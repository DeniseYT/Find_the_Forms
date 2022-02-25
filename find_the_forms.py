from bs4 import BeautifulSoup #pull the data from html file
import requests #fetch from html file
import lxml #parse or translate html to python and manipulated
import pandas as pd #manipulate the data, print info and save into a file
import pprint
import os


#Testing if connected
search_url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"

#HTTP GET requests
page = requests.get(search_url)
print(page) #<Response [200]> to test the url and it's ok

#Checking if we successfully fetched the URL 
if page.status_code == requests.codes.ok:
    print("We fetch the url!")
    # we need to translate it to python
    bs= BeautifulSoup(page.text, "lxml")
    # print(bs)
    list_all_forms = bs.findAll("table", class_="picklist-dataTable")
    list_all_forms = bs.findAll("div", class_="picklistTable")
    # print(list_all_forms)
    # print(len(list_all_forms))

    form = list_all_forms
    # print(form)


#Data 
data = []
year_list = []
result = {
        "form_number": "",
        "form_title": "",
        "min_year": "",
        "max_year": ""
        }


def download_data(pdf_url, form_number, year):
    """download pdf files from IRS website and save it to the folder"""

    r = requests.get(pdf_url, stream = True)
    
    try:
        os.mkdir(form_number)
    except:
        pass

    with open(f'{form_number}/{form_number} - {year}.pdf', "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)


def find(searching_url):
    """Search from the searching_url for forms."""

    req = requests.get(searching_url)
    
    if req.status_code == requests.codes.ok:
        soup = BeautifulSoup(req.content, "html.parser")
        all_rows = soup.findAll("tr")
        
        for row in all_rows[5:]:
            form_number = row.find(class_="LeftCellSpacer").get_text(strip=True)
            # print(form_number) #Form 1095-C

            form_title = row.find(class_="MiddleCellSpacer").get_text(strip=True)
            # print(form_title) #Employer-Provided Health Insurance Offer and Coverage

            year = row.find(class_= 'EndCellSpacer').get_text(strip=True)
            # print(year) #2021

            pdf_url = row.find(class_='LeftCellSpacer').find('a')['href']

            if form_number.lower() == item.lower():
                result["form_number"] = form_number
                result["form_title"] = form_title
                year_list.append(year)

                if download.lower() == "y":
                    for print_year in print_years:
                        if print_year == int(year):
                            print(f"downloading now for {print_year}")
                            download_data(pdf_url, form_number, year)
        
        if soup.find(class_="errorBlock"):
            print("No result")
            return
        
        elif soup.find(class_="NumPageViewed").find_all("a"):
            next_page_text = soup.find("th", class_="NumPageViewed").find_all("a")[-1].text

            if next_page_text == "Next »":
                next_page_partial = soup.find("th", class_="NumPageViewed").find_all("a")[-1]["href"]
                next_page_url = base_url + next_page_partial
                find(next_page_url)
                return

    result["min_year"] = year_list[-1]
    result["max_year"] = year_list[0]
    data.append(result.copy())
    return data



#Asking few questions
search = input("Which form number are you looking for? \nForm W-2, Form 1095-C, Form W-3 ...etc.\n>> ").split(", ")
download = input("Would you like to download them? (y/n)\n>> ")

if download == "y":
    year_range = input("What years are you looking for? ex.2018-2020\n>> ").split("-")

    if int(year_range[0]) > int(year_range[1]):
        print("Please follow the year range format!\n>> ")
        print_years = []
    else:
        print_years = [year for year in range(int(year_range[0]), int(year_range[1]) + 1)]

else:
    print_years = []



#Initial URL
base_url = "https://apps.irs.gov/"

for item in search:
    form_search = item.replace(" ", "+")

    searching_url = f"https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value={form_search}&criteria=formNumber&submitSearch=Find"
    print(f"Searching {item} from here: {searching_url}\n")
    find(searching_url)

print("Completed")

if print == "y":
    print("Succesfully download pdf files")

print("Show data: \n")
print(f"{pprint.pprint(data)}")










            
