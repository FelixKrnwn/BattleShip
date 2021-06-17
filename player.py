

class Player:

	def __init__(self, name='John'):
		self.name = name
		self.score = 0
		self.steps = 0

	def current_location(self, pos_x, pos_y):
		self.location = (pos_x, pos_y)