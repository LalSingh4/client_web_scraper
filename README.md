client_web_scraper
This project consists of three compinents: a client,  a web service built with FastAPI and a scrape.
The client prompts the user to enter the url of a webpage containing movies title ,Then sends a requests to the web service which scrapes the movies title from the provider url using the scrape and return them to client

Run the web service:
uvicorn web_service:app==reload

Run the client:
python client.py
Enter the URL of the webpage containg the movies title when prompted
