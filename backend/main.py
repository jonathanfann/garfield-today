from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import methods.scraper as scraper

app = FastAPI()

origins = [
    "http://hey.now:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://hey.now"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/garfield")
def read_root():
    return {"data": scraper.handle_scrape()}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}