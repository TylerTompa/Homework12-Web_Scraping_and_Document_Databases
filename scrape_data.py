####################################################################################################
"""
Tyler Tompa
2018, November, 30
UNCC Data Analytics Boot Camp Homework 12- Web Scraping and Document Databases
"""
####################################################################################################

import pymongo

from flask import Flask, render_template

connection = "mongodb://localhost:27017"
print("made connection")

client = pymongo.MongoClient(connection)
print("defined client")

database = client.mars_database
print("defined database")

database.mars_data.drop()
print("dropped if existing")

mars_data = 

database.mars_data.insert_many (
    [
        scrape()

    ]
)
print("inserted many")



# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html", text="Mars")

# @app.route("/scrape")
# def scrape_route():
#     mars_dictionary = scrape()
#     return jsonify(mars_dictionary)

# if __name__ == "__main__":
#     app.run(debug=True)