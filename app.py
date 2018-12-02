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

import sys

app = Flask(__name__)

# Here we use PyMongo to establish a Mongo connection and create a new database named mars_database.
mongo = PyMongo(app, uri= "mongodb://localhost:27017/mars_database")

# Here we print a statement so that we can look in our console to tell whether our code is working as intended.
print("####################################################################################################")
print("define mongo")
print("####################################################################################################")

@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()

    return render_template("index.html", mars = mars_data)

    # Here we print a statement so that we can look in our console to tell whether our code is working as intended.
    # In order to print statements on a flask page, we must use the sys library and print to stdout.
    print("####################################################################################################", file=sys.stdout)
    print("Load home page", file=sys.stdout)
    print("####################################################################################################", file=sys.stdout)

@app.route("/scrape")
def scrape():

    # We import the scrape_mars .py file we already created,
    # and use the scrape() function we defined therein.
    scraped_mars_data = scrape_mars.scrape()

    # Here we print a statement so that we can look in our console to tell whether our code is working as intended.
    # In order to print statements on a flask page, we must use the sys library and print to stdout.
    print("####################################################################################################", file=sys.stdout)
    print("Run scrape function", file=sys.stdout)
    print("####################################################################################################", file=sys.stdout)
    
    # We update our MongoDB database with the data which we scraped in our scrape_mars.py file.
    mongo.db.collection.update({}, scraped_mars_data, upsert=True)

    # Here we print a statement so that we can look in our console to tell whether our code is working as intended.
    # In order to print statements on a flask page, we must use the sys library and print to stdout.
    print("####################################################################################################", file=sys.stdout)
    print("####################################################################################################", file=sys.stdout)
    print("Update databse", file=sys.stdout)
    print("####################################################################################################", file=sys.stdout)

    return redirect("/")

    ## Here we print a statement so that we can look in our console to tell whether our code is working as intended.
    # In order to print statements on a flask page, we must use the sys library and print to stdout.
    print("####################################################################################################", file=sys.stdout)
    print("Redirect to index", file=sys.stdout)
    print("####################################################################################################", file=sys.stdout)

if __name__ == "__main__":
    app.run(debug=True)