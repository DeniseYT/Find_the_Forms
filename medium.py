from bs4 import BeautifulSoup #pull the data from html file
import requests #fetch from html file
import lxml #parse or translate html to python and manipulated
import pandas as pd #manipulate the data, print info and save into a file
import pprint
import os

# search_url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"
search_url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value=Form+1095-C&criteria=formNumber&submitSearch=Find"

#HTTP GET requests
page = requests.get(search_url)
print(page) #<Response [200]> to test the url and it's ok

#Checking if we successfully fetched the URL 
if page.status_code == requests.codes.ok:
    print("we fetch the url")
    # we need to translate it to python
    bs= BeautifulSoup(page.text, "lxml")
    # print(bs)
    list_all_forms = bs.findAll("table", class_="picklist-dataTable")
    list_all_forms = bs.findAll("div", class_="picklistTable")
    # print(list_all_forms)
    # print(len(list_all_forms))

    form = list_all_forms
    # print(form)

    data = {

            "form_number": [],
            "form_title": [],
            "form_year": []

    }
    

    for form in list_all_forms:

        form_name = form.find("td", class_="LeftCellSpacer").find("a").text
        print(form_name) #Form 1095-C

        form_title = form.find("td", class_="MiddleCellSpacer").text
        print(form_title) #Employer-Provided Health Insurance Offer and Coverage

        form_year = form.find("td", class_="EndCellSpacer").text
        print(form_year) #2021

        form_year = form.find("td", class_="EndCellSpacer").text
        if form_year == "2018":
            data[form_year].append(form_year)

            # data["form_number"].append(form_name)
            # data["form_title"].append(form_title)
            # data["form_year"].append(form_year)

        # print(data)
