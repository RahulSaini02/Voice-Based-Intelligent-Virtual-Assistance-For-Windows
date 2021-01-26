from newsapi import NewsApiClient  # pip install  newsapi-python
import os
from dotenv import load_dotenv

load_dotenv()

def getHeadlines():
    news_api = os.getenv("NEWS_API") 
    newsapi = NewsApiClient(api_key=news_api)
    data = newsapi.get_top_headlines(q='india', language='en', page_size=4)

    articles = data['articles']
    headline = []
    for x, y in enumerate(articles):
        id = x
        headline.append({y["title"]})
    return headline
