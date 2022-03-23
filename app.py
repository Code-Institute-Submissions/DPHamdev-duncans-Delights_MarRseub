import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# Upload import
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# root
@app.route("/")
# recipe page
@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("search.html", recipes=recipes)


# register function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check to see if username exists on
        user_exist = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if user_exist:
            flash(
                "That name already exists, think of another cool name!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        # create a users session cookie

        session["user"] = request.form.get("username").lower()
        flash("Registration sucessful")
        return redirect(url_for(
            "profile", username=session["user"]))

    return render_template("register.html")


# login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checking username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # make sure password matches
            if check_password_hash(
            existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()   
                flash("Welcome to Duncan's Delights {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # incorrect password match
                flash("Sorry, your Username and/or Password don't match")
                return redirect(url_for("login"))

        else:
        # username doesn't exist function
            flash("Sorry, your Username and/or Password don't match")
            return redirect(url_for("login"))

    return render_template("login.html")


# logout function
@app.route("/logout")
def logout():
    # log out functionality
    flash("You have logged out, come back soon!")
    session.pop("user")
    return redirect(url_for("login"))


# profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # using the user session's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        recipe = list(mongo.db.recipes.find())
        return render_template(
            "profile.html", username=username, recipes=recipe)

    return redirect(url_for("login"))


# add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":

        recipe = {
            "course_category": request.form.get("course_category"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "s_desc": request.form.get("s_desc"),
            "ingredients": request.form.get("ingredients").splitlines(),
            "directions": request.form.get("directions").splitlines(),
            "cook_tip": request.form.get("cook_tip"),
            "image_upload": request.form.get("image_upload"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)

        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    categories = mongo.db.recipeCategory.find().sort("course_category", 1)
    return render_template("addrecipe.html", categories=categories)


# edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
                "course_category": request.form.get("course_category"),
                "recipe_name": request.form.get("recipe_name"),
                "prep_time": request.form.get("prep_time"),
                "cooking_time": request.form.get("cooking_time"),
                "serves": request.form.get("serves"),
                "s_desc": request.form.get("s_desc"),
                "ingredients": request.form.get("ingredients").splitlines(),
                "directions": request.form.get("directions").splitlines(),
                "cook_tip": request.form.get("cook_tip"),
                "image_upload": request.form.get("image_upload"),
                "created_by": session["user"]
            }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)

        flash("Recipe Successfully Edited")

    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.recipeCategory.find().sort("course_category", 1)
    return render_template(
            "editrecipe.html", recipe=recipe,
            username=username, categories=categories)


# delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    if session["user"]:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        flash("Recipe Successfully Deleted")
        return redirect(url_for("profile", username=username))
    flash("Recipe Successfully Deleted")
    return redirect(url_for("profile"))


# categories
@app.route("/manage_categories")
def manage_categories():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if username != "admin":
        redirect(url_for('profile', username=username))

    categories = list(mongo.db.recipeCategory.find().sort(
        "course_category", 1))
    return render_template("recipecategory.html", categories=categories)


# add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if username != "admin":
        redirect(url_for('profile', username=username))

    if request.method == "POST":
        category = {
            "course_category": request.form.get("course_category")
        }
        mongo.db.recipeCategory.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("manage_categories"))

    return render_template("addcategory.html")


# edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "course_category": request.form.get("course_category")
        }
        mongo.db.recipeCategory.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Edited Successfully")
        return redirect(url_for("manage_categories"))

    category = mongo.db.recipeCategory.find_one({"_id": ObjectId(category_id)})
    return render_template("editcategory.html", category=category)


# delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.recipeCategory.remove({"_id": ObjectId(category_id)})
    flash("Category deleted successfully")
    return redirect(url_for("manage_categories"))


# starter page
@app.route("/starters")
def starters():
    recipe = list(mongo.db.recipes.find())
    return render_template("starters.html", recipes=recipe)


# main course page
@app.route("/mCourse")
def mCourse():
    recipe = list(mongo.db.recipes.find())
    return render_template("maincourses.html", recipes=recipe)


# dessert page
@app.route("/dessert")
def dessert():
    recipe = list(mongo.db.recipes.find())
    return render_template("desserts.html", recipes=recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            )
