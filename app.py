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
            'ingredient_1': request.form.get('ingredient_1'),
            'ingredient_2': request.form.get('ingredient_2'),
            'ingredient_3': request.form.get('ingredient_3'),
            'ingredient_4': request.form.get('ingredient_4'),
            'ingredient_5': request.form.get('ingredient_5'),
            'ingredient_6': request.form.get('ingredient_6'),
            'ingredient_7': request.form.get('ingredient_7'),
            'ingredient_8': request.form.get('ingredient_8'),
            'ingredient_9': request.form.get('ingredient_9'),
            'ingredient_10': request.form.get('ingredient_10'),
            'method_part_one': request.form.get('method_part_one'),
            'method_part_two': request.form.get('method_part_two'),
            'method_part_three': request.form.get('method_part_three'),
            'tags': request.form.getlist('tags'),
            'recipe_image': request.form.get('recipe_image')
            }
    recipes = mongo.db.recipes
    recipes.insert_one(recipe)
    return redirect(url_for('recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
