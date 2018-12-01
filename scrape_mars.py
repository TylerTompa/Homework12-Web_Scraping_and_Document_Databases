####################################################################################################
"""
Tyler Tompa
2018, November, 30
UNCC Data Analytics Boot Camp Homework 12- Web Scraping and Document Databases
"""
####################################################################################################

import os

from bs4 import BeautifulSoup as bs
import requests

import pandas as pd

def scrape():
    nasa_mars_file_path = os.path.join("NewsNASAMarsExplorationProgram", "News_NASA_Mars_Exploration_Program.html")
    nasa_mars_html = open(nasa_mars_file_path, "r").read()

    nasa_news_site_soup = bs(nasa_mars_html, "html.parser")

    nasa_news_article_titles_html = nasa_news_site_soup.find_all("div", class_="content_title")
    nasa_news_article_paragraphs_html = nasa_news_site_soup.find_all("div", class_="article_teaser_body")

    nasa_news_article_titles_list = []
    nasa_news_article_paragraphs_list = []

    nasa_news_article_title = nasa_news_article_titles_html[0].find("a").text
    nasa_news_article_title

    nasa_news_article_paragraph = nasa_news_article_paragraphs_html[0].text.replace("\n", "")
    nasa_news_article_paragraph

    featured_mage_base_url = "https://www.jpl.nasa.gov"
    featured_image_starting_site_extension = "/spaceimages/?search=&category=Mars"

    site_with_featured_image_url = featured_mage_base_url + featured_image_starting_site_extension
    featured_image_site = requests.get(site_with_featured_image_url)
    featured_image_soup = bs(featured_image_site.text, "html.parser")

    featured_image_url_extension = featured_image_soup.find("a", class_=["button", "fancybox"]).get("data-fancybox-href")
    featured_image_url_extension

    featured_image_url = featured_mage_base_url + featured_image_url_extension
    featured_image_url

    mars_twitter_page = requests.get("https://twitter.com/marswxreport?lang=en")
    mars_twitter_page


    mars_twitter_page_soup = bs(mars_twitter_page.text, "html.parser")

    mars_twitter_page_latest_tweet = mars_twitter_page_soup.find("p", class_="TweetTextSize").text
    mars_twitter_page_latest_tweet

    mars_twitter_page_latest_tweet_dictionary = {"latest_tweet": mars_twitter_page_latest_tweet}
    mars_twitter_page_latest_tweet_dictionary

    mars_space_facts_url = "https://space-facts.com/mars/"

    mars_facts_tables = pd.read_html(mars_space_facts_url)

    mars_facts_tables

    type(mars_facts_tables)
    len(mars_facts_tables)

    mars_facts_tables[0]

    mars_facts_table = mars_facts_tables[0]
    mars_facts_table

    mars_facts_html_table_string = mars_facts_tables[0].to_html()

    mars_facts_html_table_string

    cerebrus_hemisphere_site = requests.get("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    cerebrus_hemisphere_site

    cerebrus_hemisphere_soup = bs(cerebrus_hemisphere_site.text, "html.parser")

    schiaparelli_hemisphere_site = requests.get("https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced")
    schiaparelli_hemisphere_site

    schiaparelli_hemisphere_soup = bs(schiaparelli_hemisphere_site.text, "html.parser")

    syrtis_major_hemisphere_site = requests.get("https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced")
    syrtis_major_hemisphere_site

    syrtis_major_hemisphere_soup = bs(syrtis_major_hemisphere_site.text, "html.parser")

    valles_marineris_hemisphere_site = requests.get("https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced")
    valles_marineris_hemisphere_site

    valles_marineris_hemisphere_soup = bs(valles_marineris_hemisphere_site.text, "html.parser")

    mars_hemisphere_soups_list = [cerebrus_hemisphere_soup, schiaparelli_hemisphere_soup, syrtis_major_hemisphere_soup, valles_marineris_hemisphere_soup]

    mars_hemisphere_images_list = [mars_hemisphere.find("div", class_="downloads") for mars_hemisphere in mars_hemisphere_soups_list]

    mars_hemisphere_image_urls_list = [mars_hemisphere_image.find("a").get("href") for mars_hemisphere_image in mars_hemisphere_images_list]
    mars_hemisphere_image_urls_list

    mars_hemisphere_names_list = ["Cerberus", "Schiaparelli", "Syrtis_Major", "Valles_Marineris"] 

    mars_hemisphere_name_and_image_urls_dictionary = dict(zip(mars_hemisphere_names_list, mars_hemisphere_image_urls_list))
    mars_hemisphere_name_and_image_urls_dictionary

    mars_data_dictionary = {"latest_article_title": nasa_news_article_title,
                            "latest_artitle_paragraph": nasa_news_article_paragraph,
                            "featured_image_url": featured_image_url,
                            "latest_weather_tweet": mars_twitter_page_latest_tweet,
                            "mars_facts_table": mars_facts_table,
                            "cerberus_hemisphere_image_url": mars_hemisphere_image_urls_list[0],
                            "schiaparelli_hemisphere_image_url": mars_hemisphere_image_urls_list[1],
                            "syrtis_major_hemisphere_image_url": mars_hemisphere_image_urls_list[2],
                            "valles_marineris_hemisphere_image_url": mars_hemisphere_image_urls_list[3]                       
                        }
   
    return mars_data_dictionary

    print(mars_data_dictionary)

print(scrape)
scrape()

