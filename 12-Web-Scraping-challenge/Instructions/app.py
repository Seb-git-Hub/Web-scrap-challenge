from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
app.config ["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# set up routes
@app.route('/scrape')
def scraper():
    mars=mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    print(mars_data)
    #return "Scraping Successful"
    return redirect("/", code=302)
   
app.route("/")
def index():
    mars_data = mongo.db.mars_app.find_one()    
    return render_template("index.html", data=mars_data)


if __name__ == "__main__":
    app.run(debug=True)

