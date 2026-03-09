from fastapi import FastAPI
from typing import Literal
from api.models import Article
from api.scraper import scrape_hackernews
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

app = FastAPI(
    title="HackerNews Scraper API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "HackerNews Scraper API"}

@app.get("/top", response_model=list[Article])
def get_top(pages: int = 1, sort: Literal["score", "comments"] = "score"):
    articles_data = scrape_hackernews(pages)
    
    articles_data = sorted(
        articles_data,
        key=lambda article: article[sort],
        reverse=True
    )
    
    return articles_data