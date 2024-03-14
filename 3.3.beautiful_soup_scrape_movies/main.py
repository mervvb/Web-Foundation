import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
movie_web_page = response.text
soup = BeautifulSoup(movie_web_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
#print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("3.3.beautiful_soup_scrape_movies/movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")