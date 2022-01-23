# Tutorial 1

# from bs4 import BeautifulSoup

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

# tag = doc.title 
# print(tag) #<title>Your Title Here</title>
# print(tag.string) #Your Title Here

# #if like to modify
# tag.string = "hello"
# print(tag) #<title>hello</title>

# #if like to find all something
# tags = doc.find_all("p")
# print(tags) #print all the <p> tag
# tags = doc.find_all("p")[0]
# print(tags.find_all("b")) #nested list



# Tutorial 4
# from bs4 import BeautifulSoup
# import requests
# import re #regular expression

# year = input("What year of form are you searching for? ")
# url = f"https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value={year}&criteria=currentYearRevDateString&submitSearch=Find"
# # url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"
# page = requests.get(url).text
# doc = BeautifulSoup(page, "html.parser")

# page_text = doc.find(class_="paginationBottom")
# print(page_text)


# Tutorial 3
from bs4 import BeautifulSoup
import requests

url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
# print(tbody)
trs = tbody.contents
print(trs)

