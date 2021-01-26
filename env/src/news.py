from newsapi import NewsApiClient  # pip install  newsapi-python
import os
from dotenv import load_dotenv

load_dotenv()

def getNews(audio):
    news_api = os.getenv("NEWS_API") 
    newsapi = NewsApiClient(api_key=news_api)
    data = newsapi.get_top_headlines(q=audio,language='en',page_size=4)

    articles = data['articles']
    news = []
    for x,y in enumerate(articles):
        id = x
        news.append({y["title"]})
        
    return news

