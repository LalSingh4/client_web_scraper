from scrape import ScrapeSite
from fastapi import FastAPI

app = FastAPI()

@app.get("/get_movie")
async def get_movie(url):
    #Create instance of ScrapeSite class
    scrape = ScrapeSite()
    #Call the scrape site
    movie_list = scrape.scrape_site(url)
    return {"movies_title":movie_list}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
