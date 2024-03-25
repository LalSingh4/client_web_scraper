import requests

def main(url):
    # Send a get request to the fastapi webservice endpoint with the provider url
    response = requests.get(f"http://127.0.0.1:8000/get_movies?url={url}")
    #Parse the json response into Dictionary
    movie_data = response.json()
    movies_title = movie_data.get("movies_title")
    print("movies_title:")
    for title in movies_title:
        print(title)
     
    
    
    
if __name__ == "__main__":
    # User to enter the url of webpage containing movies title
    url = input("enter the url of website:")
    main(url)     