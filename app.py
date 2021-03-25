from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from restful.controllers.Recipes import *
from restful.controllers.Drinks import DrinksController

app = Flask(__name__)
api = Api(app)

api.add_resource(RecipesController, "/recipes")
api.add_resource(RecipeController, "/recipes/<recipe_id>")

if __name__ == '__main__':
	recipes = RecipesController
	app.run(port='5000')