from typing import Union

from fastapi import FastAPI
from facebook_scraper import get_posts

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{page_id}")
def scrap_item(page_id: str):
    for post in get_posts(page_id, pages=2):
        return {"posts": post}