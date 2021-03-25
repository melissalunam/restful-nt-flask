from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from restful.controllers.Recipes import RecipesController
from restful.controllers.Drinks import DrinksController

app = Flask(__name__)
api = Api(app)

api.add_resource(RecipesController, "/")

if __name__ == '__main__':
	recipes = RecipesController
	app.run(port='5000')