
import os

from bs4 import BeautifulSoup as bs
import requests


import pandas as pd

def scrape():


    # ## In this section we scrape the NASA Mars news site:
    # https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

    # In[2]:


    nasa_mars_file_path = os.path.join("NewsNASAMarsExplorationProgram", "News_NASA_Mars_Exploration_Program.html")
    nasa_mars_html = open(nasa_mars_file_path, "r").read()


    # In[3]:


    nasa_news_site_soup = bs(nasa_mars_html, "html.parser")


    # In[4]:


    nasa_news_article_titles_html = nasa_news_site_soup.find_all("div", class_="content_title")
    nasa_news_article_paragraphs_html = nasa_news_site_soup.find_all("div", class_="article_teaser_body")


    # In[5]:


    nasa_news_article_titles_list = []
    nasa_news_article_paragraphs_list = []


    # In[6]:


    nasa_news_article_title = nasa_news_article_titles_html[0].find("a").text
    nasa_news_article_title


    # In[7]:


    nasa_news_article_paragraph = nasa_news_article_paragraphs_html[0].text.replace("\n", "")
    nasa_news_article_paragraph


    # In[8]:


    # I misunderstood the directions and created a list of all the article titles.
    # Here I comment out the code that made the list.

    # for nasa_news_article_title in nasa_news_article_titles_html:
    #     try:
    #         nasa_news_article_titles_list.append(nasa_news_article_title.find("a").text.strip())

            
    #     except:
    #         print("Error")


    # In[9]:


    # I misunderstood the directions and created a list of all the article paragraphs.
    # Here I comment out the code that made the list.

    # for nasa_news_article_paragraph in nasa_news_article_paragraphs_html:
    #     try:
    #         nasa_news_article_paragraphs_list.append(nasa_news_article_paragraph.text.replace("\n", ""))
            
    #     except:
    #         print("Error")


    # In[10]:


    # I misunderstood the directions and created a list of all the article titles and paragraphs.
    # Here I comment out the code that makes a dictionary from the two lists.

    # nasa_news_articles_dictionary = dict(zip(nasa_news_article_titles_list, nasa_news_article_paragraphs_list))
    # nasa_news_articles_dictionary


    # ## In this section we scrape the URL for a featured image

    # In[11]:


    featured_mage_base_url = "https://www.jpl.nasa.gov"
    featured_image_starting_site_extension = "/spaceimages/?search=&category=Mars"

    site_with_featured_image_url = featured_mage_base_url + featured_image_starting_site_extension
    featured_image_site = requests.get(site_with_featured_image_url)
    featured_image_soup = bs(featured_image_site.text, "html.parser")


    # In[12]:


    featured_image_url_extension = featured_image_soup.find("a", class_=["button", "fancybox"]).get("data-fancybox-href")
    featured_image_url_extension


    # In[13]:


    featured_image_url = featured_mage_base_url + featured_image_url_extension
    featured_image_url


    # ## In this section we scrape tweets from the @MarsWxReport Twitter account to get the latest weather on Mars: https://twitter.com/marswxreport?lang=en

    # In[14]:


    mars_twitter_page = requests.get("https://twitter.com/marswxreport?lang=en")
    mars_twitter_page


    # In[15]:


    mars_twitter_page_soup = bs(mars_twitter_page.text, "html.parser")


    # In[16]:


    mars_twitter_page_latest_tweet = mars_twitter_page_soup.find("p", class_="TweetTextSize").text
    mars_twitter_page_latest_tweet


    # In[17]:


    mars_twitter_page_latest_tweet_dictionary = {"latest_tweet": mars_twitter_page_latest_tweet}
    mars_twitter_page_latest_tweet_dictionary


    # ## In this section we use pandas to directly scrape data from the Mars Facts website: https://space-facts.com/mars/

    # In[18]:


    mars_space_facts_url = "https://space-facts.com/mars/"


    # In[19]:


    mars_facts_tables = pd.read_html(mars_space_facts_url)


    # In[20]:


    mars_facts_tables


    # In[21]:


    type(mars_facts_tables)


    # In[22]:


    len(mars_facts_tables)


    # In[23]:


    mars_facts_tables[0]


    # In[24]:


    mars_facts_table_dataframe = mars_facts_tables[0]
    mars_facts_table_dataframe


    # In[25]:


    mars_facts_table_dataframe = mars_facts_table_dataframe.set_index([0])
    mars_facts_table_dataframe


    # In[26]:


    mars_facts_table_dataframe["Values"] = mars_facts_table_dataframe[1]
    mars_facts_table_dataframe = mars_facts_table_dataframe.drop(mars_facts_table_dataframe.columns[0], axis=1)
    mars_facts_table_dataframe


    # In[27]:


    mars_facts_table_dataframe.index.rename("Description", inplace=True)


    # In[28]:


    mars_facts_table_dataframe


    # In[29]:


    mars_facts_html_table_string = mars_facts_table_dataframe.to_html()


    # In[30]:


    mars_facts_html_table_string


    # In[31]:


    type(mars_facts_html_table_string)


    # In[32]:


    mars_facts_table_json = mars_facts_table_dataframe.to_json()
    mars_facts_table_json


    # ## In this section we visit the USGS Astrogeology site to obtain high resolution images for each of Mars's hemispheres.

    # In[33]:


    cerebrus_hemisphere_site = requests.get("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    cerebrus_hemisphere_site


    # In[34]:


    cerebrus_hemisphere_soup = bs(cerebrus_hemisphere_site.text, "html.parser")


    # In[35]:


    schiaparelli_hemisphere_site = requests.get("https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced")
    schiaparelli_hemisphere_site


    # In[36]:


    schiaparelli_hemisphere_soup = bs(schiaparelli_hemisphere_site.text, "html.parser")


    # In[37]:


    syrtis_major_hemisphere_site = requests.get("https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced")
    syrtis_major_hemisphere_site


    # In[38]:


    syrtis_major_hemisphere_soup = bs(syrtis_major_hemisphere_site.text, "html.parser")


    # In[39]:


    valles_marineris_hemisphere_site = requests.get("https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced")
    valles_marineris_hemisphere_site


    # In[40]:


    valles_marineris_hemisphere_soup = bs(valles_marineris_hemisphere_site.text, "html.parser")


    # In[41]:


    mars_hemisphere_soups_list = [cerebrus_hemisphere_soup, schiaparelli_hemisphere_soup, syrtis_major_hemisphere_soup, valles_marineris_hemisphere_soup]


    # In[42]:


    mars_hemisphere_images_list = [mars_hemisphere.find("div", class_="downloads") for mars_hemisphere in mars_hemisphere_soups_list]


    # In[43]:


    mars_hemisphere_image_urls_list = [mars_hemisphere_image.find("a").get("href") for mars_hemisphere_image in mars_hemisphere_images_list]
    mars_hemisphere_image_urls_list


    # In[44]:


    mars_hemisphere_names_list = ["Cerberus", "Schiaparelli", "Syrtis_Major", "Valles_Marineris"] 


    # In[45]:


    mars_hemisphere_name_and_image_urls_dictionary = dict(zip(mars_hemisphere_names_list, mars_hemisphere_image_urls_list))
    mars_hemisphere_name_and_image_urls_dictionary


    # In[46]:


    # I tried to make a dictionary of the hemisphere names and image URLs by doing this.
    # This did not have the desired results, so I will comment it out for now.

    # mars_hemisphere_name_and_image_urls_dictionary = {"Name": hemisphere_name, "image_url": hemisphere_image_url \
    #                                                   for hemisphere_name, hemisphere_image_url \
    #                                                   in mars_hemisphere_names_list, mars_hemisphere_image_urls_list}


    # ## In this section, we create a dictionary of all the data we have scraped hitherto.

    # In[47]:


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

