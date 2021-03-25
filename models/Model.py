from sqlalchemy import create_engine

class Model:
	def __init__(self):
		self.db = create_engine('sqlite:///recipes_db.db').connect()