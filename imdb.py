from bs4 import BeautifulSoup
import requests

source = requests.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html")
source.raise_for_status()

soup = BeautifulSoup(source.text, "html.parser")

forms = soup.find("table", class_="picklist-dataTable").find_all("tr")
# print(len(forms))

for form in forms:

    form_name = form.find("th", class_="FormNumber").a.text
    # form_name = form.find("td", class_="LeftCellSpacer").a.text
    print(form_name) #Product Number

    form_title = form.find("th", class_="Title").a.text
    print(form_title) #Title

    form_year = form.find("th", class_="CurrentYear").a.text
    print(form_year) #Revision Date
    
    break


# except Exception as e:
#     print(e)