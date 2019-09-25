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
            'serves': request.form.get('serves'),
            'difficulty': request.form.get('difficulty'),
            'description': request.form.get('description'),
            'ingredients': request.form.getlist('ingredients'),
            'method_part_one': request.form.get('method_part_one'),
            'method_part_two': request.form.get('method_part_two'),
            'method_part_three': request.form.get('method_part_three'),
            'recipe_image': request.form.get('recipe_image')
            }
    recipes = mongo.db.recipes
    recipes.insert_one(recipe)
    return redirect(url_for('recipes'))
    
@app.route('/full_recipe/<recipes_id>')
def full_recipe(recipes_id):
    the_full_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_cuisines = mongo.db.cuisines.find()
    return render_template('fullrecipe.html', recipes=the_full_recipe, cuisines=all_cuisines)


@app.route('/delete_recipe/<recipes_id>')
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipes_id)})
    return redirect(url_for('recipes'))
    
    
@app.route('/edit_recipe/<recipes_id>')
def edit_recipe(recipes_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_cuisines = mongo.db.cuisines.find()
    return render_template('editrecipe.html', recipes=the_recipe, cuisines=all_cuisines)
    
@app.route('/update_recipe/<recipes_id>', methods=['POST'])
def update_recipe(recipes_id):
    recipes = mongo.db.recipes
    recipes.update( {"_id": ObjectId(recipes_id)},
    {
        'name': request.form.get('name'),
        'cuisine': request.form.get('cuisine'),
        'cook_time': request.form.get('cook_time'),
        'serves': request.form.get('serves'),
        'difficulty': request.form.get('difficulty'),
        'description': request.form.get('description'),
        'ingredients': request.form.getlist('ingredients'),
        'method_part_one': request.form.get('method_part_one'),
        'method_part_two': request.form.get('method_part_two'),
        'method_part_three': request.form.get('method_part_three'),
        'recipe_image': request.form.get('recipe_image')
    })
    return redirect(url_for('recipes'))
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
