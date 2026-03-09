from bs4 import BeautifulSoup
from functools import lru_cache
import time
import requests
import logging

logger = logging.getLogger(__name__)

@lru_cache(maxsize=10)
def scrape_hackernews(pages: int) :
    
    articles_data = []
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    for i in range(1, pages + 1) :

        page_url = f"https://news.ycombinator.com/?p={i}"
        time.sleep(1)
        try:
            response = requests.get(page_url, headers=headers, timeout=10)
        except requests.exceptions.RequestException as e:
            logger.error("Request failed for %s: %s", page_url, e)
            continue
        
        if response.status_code != 200 :
            logger.warning("Bad response %s for %s", response.status_code, page_url)
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.select("tr.athing")
        logger.info("Found %s articles on page %s", len(articles), i)
        for article in articles:
            title_tag = article.select_one("span.titleline a")

            title = title_tag.text
            article_url = title_tag["href"]

            meta_row = article.find_next_sibling("tr")

            score_tag = meta_row.select_one("span.score")
            author_tag = meta_row.select_one("a.hnuser")

            score = score_tag.text if score_tag else "0 points"
            score = int(score.split()[0])
            author = author_tag.text if author_tag else "unknown"
            links = meta_row.select("a")

            comments = "0 comments"

            if links:
                last_link = links[-1].text
                if "comment" in last_link:
                    comments = last_link
            
            comments = int(comments.split()[0])

            article_data = {
                "title": title,
                "url": article_url,
                "score": score,
                "author": author,
                "comments": comments
            }

            articles_data.append(article_data)
    return articles_data