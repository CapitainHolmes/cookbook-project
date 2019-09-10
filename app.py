import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", cuisines=mongo.db.cuisines.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = {
            'name': request.form.get('name'),
            'cuisine': request.form.get('cuisine'),
            'cook_time': request.form.get('cook_time'),
            'sevres': request.form.get('serves'),
            'difficulty': request.form.get('difficulty'),
            'description': request.form.get('description'),
            'tags': request.form.getlist('tags')
            }
    recipes = mongo.db.recipes
    recipes.insert_one(recipe)
    return redirect(url_for('recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
