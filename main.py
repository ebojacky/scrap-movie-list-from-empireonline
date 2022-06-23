import requests
from bs4 import BeautifulSoup
import pprint
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
top_movies = soup.findAll(name="h3", class_="title")
formatted_top_movies = [movie.text for movie in top_movies]
reversed_top_movies = formatted_top_movies[::-1]
pprint.pprint(reversed_top_movies)


