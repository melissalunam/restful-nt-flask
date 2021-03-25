from flask import Flask, request, jsonify
from restful.models.Recipes import RecipesModel

app = Flask(__name__)

@app.route("/recipes", methods=['GET', 'POST'])
def getRecipes():
	#Se retornan todos los valores de recipes
	if request.method == 'GET':
		return jsonify(RecipesModel().all()), 200
	elif request.method == 'POST':
		return "Aqui es la logica para hacer post"

if __name__ == '__main__':
	recipes = RecipesController
	app.run(port='5000')