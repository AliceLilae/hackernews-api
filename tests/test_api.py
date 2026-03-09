from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "HackerNews Scraper API"}
    
def test_top_endpoint():
    response = client.get("/top")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    if len(data) > 0:
        article = data[0]
        assert "title" in article
        assert "score" in article
        assert "url" in article
        assert "author" in article
        assert "comments" in article