from flask_restful import Resource, Api

class RecipesController(Resource):
	def get(self):
		return "Recipes"