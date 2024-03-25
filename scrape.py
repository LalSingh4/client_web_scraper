from bs4 import BeautifulSoup
import requests

class ScrapeSite:
    def __init__(self):
        pass
    
    def scrape_site(self, url):
        #Send a get request to specific url
        response = requests.get(url)
        website_html = response.text
        soup = BeautifulSoup(website_html, "html.parser")
        #find all the movies title in html
        all_movies = soup.find_all(name="h3", class_="title")
        #Extract the text of each movies title
        movies_title = [movie.getText() for movie in all_movies]
        movies = movies_title[::-1]
        return movies
    