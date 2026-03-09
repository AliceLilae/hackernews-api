from pydantic import BaseModel

class Article(BaseModel):
    title: str
    url: str
    score: int
    author: str
    comments: int