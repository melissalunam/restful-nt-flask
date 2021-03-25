from restful.models.Model import Model as model
from sqlalchemy import create_engine

class RecipesModel(model):

	table = 'recipes'
	fillable = ['name', 'description', 'ingredients', 'preparation']

	def __init__(self):
		model.__init__(self)

	def all(self):
		data = self.db.execute("SELECT * FROM recipes")
		return { "recipes": [dict(zip(tuple (data.keys()), i)) for i in data.cursor]}
