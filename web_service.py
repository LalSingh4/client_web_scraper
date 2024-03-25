from scrape import ScrapeSite
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
class URLInput(BaseModel):
    url:str

@app.get("/get_movie")
async def get_movie(url_input: URLInput):  #url_unput is instance of URLInput
    #Create instance of ScrapeSite class
    scrape = ScrapeSite(url_input.url)
    #Call the scrape site
    movie_list = scrape.scrape_site()
    return {"movies_title":movie_list}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
