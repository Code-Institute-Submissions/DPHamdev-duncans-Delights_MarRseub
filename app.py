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
# Upload authentication
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


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
                flash("Sorry, your Username and/or Password don't match.")
                return redirect(url_for("login"))

        else:
            # username doesn't exist function
            flash("Sorry, your Username and/or Password don't match")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # log out functionality
    flash("You have logged out, come back soon!")
    session.pop("user")
    return redirect(url_for("login"))

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


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


# Image Upload

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
            "directions": request.form.get("directions"),
            "cook_tip": request.form.get("cook_tip"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)

        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    categories = mongo.db.recipeCategory.find().sort("course_category", 1)
    return render_template("addrecipe.html", categories=categories)


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


# @app.route('/', methods=['POST'])
# def upload_image():
# 	if 'file' not in request.files:
# 		flash('No file part')
# 		return redirect(request.url)
# 	file = request.files['file']
# 	if file.filename == '':
# 		flash('No image selected for uploading')
# 		return redirect(request.url)
# 	if file and allowed_file(file.filename):
# 		filename = secure_filename(file.filename)
# 		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 		#print('upload_image filename: ' + filename)
# 		flash('Image successfully uploaded and displayed below')
# 		return render_template('upload.html', filename=filename)
# 	else:
# 		flash('Allowed image types are -> png, jpg, jpeg, gif')
# 		return redirect(request.url)


# @app.route('/display/<filename>')
# def display_image(filename):
# 	#print('display_image filename: ' + filename)
# 	return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
