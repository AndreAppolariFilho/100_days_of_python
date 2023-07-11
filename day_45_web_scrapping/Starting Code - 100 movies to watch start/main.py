import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

titles_elements = soup.find_all(name="h3", class_="title")

titles = [title_element.getText() for title_element in titles_elements]
titles = titles[::-1]
with open("movies.txt", "w", encoding="utf8") as file:
    file.write("\n".join(titles))


