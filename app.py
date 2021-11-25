import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/add_recipe")
def add_recipe():
    return render_template("addrecipe.html")

@app.route("/starters")
def starters():
    recipe = list(mongo.db.recipes.find())
    return render_template("starters.html", recipes=recipe)


@app.route("/mCourse")
def mCourse():
    recipe = list(mongo.db.recipes.find())
    return render_template("maincourses.html", recipes=recipe)


@app.route("/dessert")
def dessert():
    recipe = list(mongo.db.recipes.find())
    return render_template("desserts.html", recipes=recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
