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
    # ## In this section we scrape the NASA Mars news site for the latest article title and summary paragraph:
    # https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

    # We are using a local saved HTML file of the page we are scraping.
    # Here we define the file path and open the file.

    nasa_mars_file_path = os.path.join("NewsNASAMarsExplorationProgram", "News_NASA_Mars_Exploration_Program.html")
    nasa_mars_html = open(nasa_mars_file_path, "r").read()

    nasa_news_site_soup = bs(nasa_mars_html, "html.parser")

    # We scrape <div> elements with the class content_title to get the title.
    # We scrape <div> elements with the class article_teaser_body to get the summary paragraph.

    nasa_news_article_titles_html = nasa_news_site_soup.find_all("div", class_="content_title")
    nasa_news_article_paragraphs_html = nasa_news_site_soup.find_all("div", class_="article_teaser_body")

    nasa_news_article_title = nasa_news_article_titles_html[0].find("a").text
    nasa_news_article_title

    nasa_news_article_paragraph = nasa_news_article_paragraphs_html[0].text.replace("\n", "")
    nasa_news_article_paragraph

    # I misunderstood the directions and created a list of all the article titles and summary paragraphs.
    # Here I comment out the list declarations in case I want to use them later.

    # nasa_news_article_titles_list = []
    # nasa_news_article_paragraphs_list = []

    # I misunderstood the directions and created a list of all the article titles.
    # Here I comment out the code that made the list.

    # for nasa_news_article_title in nasa_news_article_titles_html:
    #     try:
    #         nasa_news_article_titles_list.append(nasa_news_article_title.find("a").text.strip())

            
    #     except:
    #         print("Error")

    # I misunderstood the directions and created a list of all the article paragraphs.
    # Here I comment out the code that made the list.

    # for nasa_news_article_paragraph in nasa_news_article_paragraphs_html:
    #     try:
    #         nasa_news_article_paragraphs_list.append(nasa_news_article_paragraph.text.replace("\n", ""))
            
    #     except:
    #         print("Error")

    # I misunderstood the directions and created a list of all the article titles and paragraphs.
    # Here I comment out the code that makes a dictionary from the two lists.

    # nasa_news_articles_dictionary = dict(zip(nasa_news_article_titles_list, nasa_news_article_paragraphs_list))
    # nasa_news_articles_dictionary


    # ## In this section we scrape the NASA JPL site for a featured image

    # The featured image is comprised of the "base" URL plus its specific URL extension.
    # We must follow another speficic URL first;
    # This will take us to a page, on which we can see a smaller "preview" image.
    # This same page includes a button which redirects to a high-quality full-size image.
    # We scrape the URL extension from this page, and append it to the base URL.

    featured_mage_base_url = "https://www.jpl.nasa.gov"
    featured_image_starting_site_extension = "/spaceimages/?search=&category=Mars"

    site_with_featured_image_url = featured_mage_base_url + featured_image_starting_site_extension
    featured_image_site = requests.get(site_with_featured_image_url)
    featured_image_soup = bs(featured_image_site.text, "html.parser")

    featured_image_url_extension = featured_image_soup.find("a", class_=["button", "fancybox"]).get("data-fancybox-href")
    featured_image_url_extension

    featured_image_url = featured_mage_base_url + featured_image_url_extension
    featured_image_url

    # ## In this section we scrape tweets from the @MarsWxReport Twitter account to get the latest weather on Mars: https://twitter.com/marswxreport?lang=en

    mars_twitter_page = requests.get("https://twitter.com/marswxreport?lang=en")
    mars_twitter_page

    mars_twitter_page_soup = bs(mars_twitter_page.text, "html.parser")

    # We scrape the latest tweet from a paragraph tag with the class "TweetTextSize."

    mars_twitter_page_latest_tweet = mars_twitter_page_soup.find("p", class_="TweetTextSize").text
    mars_twitter_page_latest_tweet


    # ## In this section we use pandas to directly scrape data from the Mars page from the Space Facts website: https://space-facts.com/mars/

    mars_space_facts_url = "https://space-facts.com/mars/"

    # The pandas library include a function titled .read_html(),
    # which directly takes a URL as an argument, and creates a list of everything it detects in a table format.

    mars_facts_tables = pd.read_html(mars_space_facts_url)

    mars_facts_tables

    type(mars_facts_tables)

    len(mars_facts_tables)

    mars_facts_tables[0]

    # The .read_html() returns a list of all the "tables" that it finds.
    # Even if pandas finds only 1 table, it will return a list with the 1 table.
    # Therefore we must create a dataframe by setting a variable equal to this item in the list.

    mars_facts_table_dataframe = mars_facts_tables[0]
    mars_facts_table_dataframe

    # This table will eventually be used on a flask webpage.
    # We will use the pandas function .to_html() to create a string with the HTML markup which would create this same table.
    # First though, we will replace the unnecessary numbered index with the more meaningful index telling us what the measurement is of.

    mars_facts_table_dataframe = mars_facts_table_dataframe.set_index([0])
    mars_facts_table_dataframe

    # Here we rename the index and the column showing us the actual values to something more meaningful.

    mars_facts_table_dataframe["Values"] = mars_facts_table_dataframe[1]

    mars_facts_table_dataframe.index.rename("Description", inplace=True)
    mars_facts_table_dataframe = mars_facts_table_dataframe.drop(mars_facts_table_dataframe.columns[0], axis=1)
    mars_facts_table_dataframe

    # Here we use the pandas functuon .to_html(),
    # to create a variable which holds the data from the dataframe as a string which produces an HTML table.

    mars_facts_html_table_string = mars_facts_table_dataframe.to_html()

    # We could also use the pandas function .to_json().
    # I leave this line commented out- but the still in place,
    # as a reminder that this function exists.

    # mars_facts_table_json = mars_facts_table_dataframe.to_json()
    # mars_facts_table_json


    # ## In this section we visit the USGS Astrogeology site to obtain high resolution images for each of Mars's hemispheres.

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

    # Here we define a list containing the BeautifulSoup for each of Mars's hemispheres.
    # We use a list comprehension which loops through this list to scrape the block of HTML which holds the URL for the image of each hemisphere.

    mars_hemisphere_soups_list = [cerebrus_hemisphere_soup, schiaparelli_hemisphere_soup, syrtis_major_hemisphere_soup, valles_marineris_hemisphere_soup]

    # Here's that list comprehension I was talking about.
    # For each hemisphere, we parse the element <div> for the class "downloads."
    # Next we will use another list comprehension which loops through this list to scrape the actual URL for each image.

    mars_hemisphere_images_list = [mars_hemisphere.find("div", class_="downloads") for mars_hemisphere in mars_hemisphere_soups_list]

    # If you didn't believe me, here it is- another list comprehension.
    # This time we find anchor elements from each block of HTML markup and get the hyperlink reference therefrom.

    mars_hemisphere_image_urls_list = [mars_hemisphere_image.find("a").get("href") for mars_hemisphere_image in mars_hemisphere_images_list]
    mars_hemisphere_image_urls_list

    # I originally misunderstood the directions, and thought I needed to make a dictionary of dictionaries at the end.
    # I intended on zippining together the list of hemisphere names with the list of each one's image URL.
    # I will leave this code commented out so that I may return to it later.

    # mars_hemisphere_names_list = ["Cerberus", "Schiaparelli", "Syrtis_Major", "Valles_Marineris"] 

    # mars_hemisphere_name_and_image_urls_dictionary = dict(zip(mars_hemisphere_names_list, mars_hemisphere_image_urls_list))
    # mars_hemisphere_name_and_image_urls_dictionary

    # I tried to make a dictionary of the hemisphere names and image URLs by doing this.
    # This did not have the desired results, so I will comment it out for now.

    # mars_hemisphere_name_and_image_urls_dictionary = {"Name": hemisphere_name, "image_url": hemisphere_image_url \
    #                                                   for hemisphere_name, hemisphere_image_url \
    #                                                   in mars_hemisphere_names_list, mars_hemisphere_image_urls_list}


    # ## In this section, we create a dictionary of all the data we have scraped hitherto.

    # We will use all the data we have scraped in a dictionary,
    # which we can then insert into MongoDB,
    # and in turn, reference from render_template for our own HTML page.

    mars_data_dictionary = {"latest_article_title": nasa_news_article_title,
                            "latest_article_paragraph": nasa_news_article_paragraph,
                            "featured_image_url": featured_image_url,
                            "latest_weather_tweet": mars_twitter_page_latest_tweet,
                            "mars_facts_table": mars_facts_html_table_string,
                            "cerberus_hemisphere_image_url": mars_hemisphere_image_urls_list[0],
                            "schiaparelli_hemisphere_image_url": mars_hemisphere_image_urls_list[1],
                            "syrtis_major_hemisphere_image_url": mars_hemisphere_image_urls_list[2],
                            "valles_marineris_hemisphere_image_url": mars_hemisphere_image_urls_list[3]                       
                        }
    mars_data_dictionary

    return mars_data_dictionary