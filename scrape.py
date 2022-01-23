import requests #fetch from html file
from bs4 import BeautifulSoup #pull the data from html file
import lxml
import json 

text_w2 = requests.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value=Form+W-2&criteria=formNumber&submitSearch=Find")
soup_w2 = BeautifulSoup(text_w2.text, "lxml")
forms_w2 = soup_w2.find_all("a")
# print(forms_w2)

data = {
        "form_number": [],
        "form_title": [],
        "min_year": [],
        "max_year": []

}


data["form_number"].append("Form W2")
data["form_title"].append("Wage and Tax Statement (Info Copy Only)")
data["min_year"].append("2018")
data["max_year"].append("2020")
# print(data)

    


text_1095c = requests.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value=Form+1095-C&criteria=formNumber&submitSearch=Find")
soup_1095c = BeautifulSoup(text_1095c.text, "lxml")
forms_1095c = soup_1095c.find_all("a")
# print(forms_1095c)


data = {

            "form_number": [],
            "form_title": [],
            "form_year": []

    }


for form in forms_1095c:
    form_year = form.find("td", class_="EndCellSpacer")
    if form_year == "2018":
        data[form_year].append(form_year)

print(data)
    