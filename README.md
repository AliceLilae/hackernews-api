# HackerNews API (FastAPI)

![Python](https://img.shields.io/badge/python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/docker-container-blue)
![pytest](https://img.shields.io/badge/tests-pytest-yellow)
![Tests](https://github.com/AliceLilae/hackernews-api/actions/workflows/tests.yml/badge.svg)

A backend API that scrapes Hacker News and exposes structured article data through a clean REST interface.

This project demonstrates backend development practices including API design, web scraping, caching, testing, structured logging, and containerized deployment.

---

# Features

* Scrapes Hacker News pages
* Extracts article metadata using BeautifulSoup
* REST API built with FastAPI
* Sorting options for results
* Response validation with Pydantic
* Caching with `functools.lru_cache`
* API tests with `pytest`
* Structured logging
* Dockerized runtime environment
* Clean and modular project structure

---

# Tech Stack

Backend

* Python
* FastAPI
* Pydantic

Scraping

* BeautifulSoup
* requests

Testing

* pytest

Infrastructure

* Docker

---

# Project Structure

Example repository structure:

```
project/
│
├─ app/
│  ├─ main.py
│  ├─ scraper.py
│  ├─ models.py
│  └─ utils.py
│
├─ tests/
│  └─ test_api.py
│
├─ Dockerfile
├─ requirements.txt
└─ README.md
```

---

# Quick Start

Clone the repository:

```
git clone https://github.com/yourusername/hackernews-api.git
cd hackernews-api
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the API:

```
uvicorn app.main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

Interactive API documentation:

```
http://localhost:8000/docs
```

---

# API Endpoint

### GET `/top`

Scrapes Hacker News and returns a list of articles.

Query parameters:

```
pages : number of Hacker News pages to scrape
sort  : sorting option (for example: score)
```

Example request:

```
/top?pages=2&sort=score
```

---

# Example Response

Example JSON response returned by the API:

```
[
  {
    "title": "Show HN: Example Project",
    "url": "https://example.com/project",
    "score": 215,
    "author": "username",
    "comments": 42
  },
  {
    "title": "Ask HN: Interesting Question",
    "url": "https://news.ycombinator.com/item?id=123456",
    "score": 98,
    "author": "another_user",
    "comments": 17
  }
]
```

Response schema defined with Pydantic:

```
class Article(BaseModel):
    title: str
    url: str
    score: int
    author: str
    comments: int
```

Using Pydantic ensures:

* response validation
* consistent API schema
* automatic documentation in Swagger UI

Source:
https://fastapi.tiangolo.com/tutorial/response-model/

---

# Architecture

High level architecture of the system:

```
Client
  │
  │ HTTP request
  ▼
FastAPI Application
  │
  │ calls
  ▼
Scraper (requests)
  │
  │ downloads HTML
  ▼
Hacker News Website
  │
  │ HTML response
  ▼
BeautifulSoup Parser
  │
  │ extract article data
  ▼
Pydantic Model
  │
  │ validation
  ▼
JSON API Response
```

Main components:

FastAPI
Handles routing, request processing and automatic API documentation.

Scraper
Downloads Hacker News pages and extracts article information.

BeautifulSoup
Parses the HTML structure of Hacker News pages.

Pydantic Models
Ensure validated and structured API responses.

Caching
`lru_cache` reduces repeated HTTP requests and improves response time.

---

# Tests

Run tests using pytest:

```
pytest
```

Tests verify API endpoints and response structure.

Source: https://docs.pytest.org/

---

# Docker

Build the Docker image:

```
docker build -t hackernews-api .
```

Run the container:

```
docker run -p 8000:8000 hackernews-api
```

The API will be available at:

```
http://localhost:8000
```

Source: https://docs.docker.com/get-started/

---

# Limitations

Current limitations of the project:

* The scraper relies on the current HTML structure of Hacker News
* No rate limiting implemented
* Caching is in-memory only
* The scraper is synchronous

---

# Roadmap

Possible future improvements:

* Async scraping using `httpx`
* Redis-based caching
* Pagination support
* Rate limiting
* CI/CD with GitHub Actions
* Cloud deployment

---

# Learning Goals

This project was built to practice and demonstrate:

* Python backend development
* REST API design
* Web scraping
* Data validation with Pydantic
* API testing
* Docker containerization
* Production-style project structure
