####################################################################################################
"""
Tyler Tompa
2018, November, 30
UNCC Data Analytics Boot Camp Homework 12- Web Scraping and Document Databases
"""
####################################################################################################

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri= "mongodb://localhost:27017/mars_database")

print("####################################################################################################")
print("define mongo")
print("####################################################################################################")

# connection = "mongodb://localhost:27017"
# client = pymongo.MongoClient(connection)
# db = client.mars_database

# db.mars.drop()

# db.mars.insert_many(
#     scrape_mars.scrape()
# )

@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()

    return render_template("index.html", mars = mars_data)

    print("####################################################################################################")
    print("Load home page")
    print("####################################################################################################")

@app.route("/scrape")
def scrape():
    scraped_mars_data = scrape_mars.scrape()
    print("####################################################################################################")
    print("Run scrape function")
    print("####################################################################################################")
    
    mongo.db.collection.update({}, scraped_mars_data, upsert=True)
    print("####################################################################################################")
    print("Update databse")
    print("####################################################################################################")

    return redirect("/")
    print("####################################################################################################")
    print("Redirect to index")
    print("####################################################################################################")

if __name__ == "__main__":
    app.run(debug=True)