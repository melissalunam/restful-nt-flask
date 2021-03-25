from flask_restful import Resource, Api

class DrinksController(Resource):
	def get(self):
		return "Drinks"