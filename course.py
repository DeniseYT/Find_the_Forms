import requests #fetch from html file
from bs4 import BeautifulSoup #pull the data from html file
import lxml

html_text = requests.get("https://apps.irs.gov/app/picklist/list/priorFormPublication.html")
soup = BeautifulSoup(html_text.text, "lxml")
# forms = soup.find_all("table", class_="picklist-dataTable")
forms = soup.find_all("a")
print(forms)


# data = [
#     {
#         "form_number": [],
#             "form_title": [],
#             "form_year": []
#     }
# ]

data = {
        "form_number": [],
        "form_title": [],
        "form_year": []

}


for form in forms:

    form_number = form.find("td", class_="LeftCellSpacer").find("a").text
    if "Form W-2" or "Form 1095-C" in form_number:
        data[form_number].append(form_number)

    form_title = form.find("td", class_="MiddleCellSpacer").text
    if "Wage and Tax Statement (Info Copy Only)" or "Employer-Provided Health Insurance Offer and Coverage" in form_number:
        data[form_title].append(form_title)

    form_year = form.find("td", class_="EndCellSpacer").text
    if "2018" or "2019" or "2020" in form_year:
        data[form_year].append(form_year)

# print(data)