from bs4 import BeautifulSoup
import lxml

with open("3.1.beautiful_soup_start/website.html", encoding="utf8") as fp:
    contents = fp.read()

soup = BeautifulSoup(contents, "lxml") #html.parser

#print(soup.title.text) #string
#print(soup.prettify())
#print(soup.a)

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))
    pass

#heading = soup.find(name="h1", id="name")
#print(heading)

section_heading = soup.find(name="h3", class_= "heading")
#print(section_heading.string)

company_url = soup.select_one(selector="p a")
#print(company_url)

name = soup.select_one(selector="#name")
#print(name)

headings = soup.select(selector=".heading")
print(headings)