from flask_restful import Resource, Api
from restful.models.Recipes import RecipesModel


class RecipesController(Resource):
	def get(self):
		return RecipesModel().all()

class RecipeController(Resource):
	def get(self, recipe_id=None):
		return "Only one Recipe"