from bs4 import BeautifulSoup
import requests

#------------------ Exercise 1
with open("website.html", encoding='utf-8') as html_file:
    html_content = html_file.read()
soup = BeautifulSoup(html_content, "html.parser")
print(soup.title.string)
print(soup.ul)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))
heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
name = soup.select_one(selector="#name")
print(name)

print(soup.select(".heading"))

#-------------------Exercise 2
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.find_all(name="a", class_="storylink"))