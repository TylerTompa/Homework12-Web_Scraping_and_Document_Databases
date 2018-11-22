from bs4 import BeautifulSoup as bs
import requests
# from splinter import Browser
# import splinter

# import pandas as pd

# nasa_news_site = requests.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest")
# nasa_news_site

# nasa_news_site_soup = bs(nasa_news_site.text, "html.parser")


# # In[4]:


# nasa_news_article_titles_html = nasa_news_site_soup.find_all("div", class_="content_title")
# nasa_news_article_paragraphs_html = nasa_news_site_soup.find_all("div", class_="'article_teaser_body")


# # In[5]:


# nasa_news_article_paragraphs_html


# # In[6]:


# nasa_news_article_titles_html


# # In[7]:


# nasa_news_article_paragraphs_html


# # In[8]:


# nasa_news_article_titles = []


# # In[9]:


# for nasa_news_article_title in nasa_news_article_titles_html:
#     try:
#         nasa_news_article_titles.append(nasa_news_article_title.find("a").text.strip())
        
#     except:
#         print("Error")


# # In[10]:


# nasa_news_article_titles

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Mission to Mars"

@app.route("/scrape")
def scrape():
    nasa_news_site = requests.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest")
    nasa_news_site_soup = bs(nasa_news_site.text, "html.parser")
    nasa_news_article_titles_html = nasa_news_site_soup.find_all("div", class_="content_title")

    nasa_news_article_titles = []

    for nasa_news_article_title in nasa_news_article_titles_html:
        try:
            nasa_news_article_titles.append(nasa_news_article_title.find("a").text.strip())
        
        except:
            print("Error")

    return nasa_news_article_titles

if __name__ == "__main__":
    app.run(debug=True)