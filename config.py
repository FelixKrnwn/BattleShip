import json

class Config:

	def __init__(self):

		#GAME CONFIG
		self.title = "Clover BATTLESHIP"
		self.row = 5
		self.column = 5


		#WINDOW CONFIG
		base = 100
		ratio = 5
		ratio1 = (3,4)
		self.side = base * ratio
		self.screen = f"{self.side}x{self.side}+500+500"
		self.width = base*ratio1[0]
		self.height = base*ratio1[1]

		#IMG PATH
		self.init_img = "img/init_img.jfif"
		self.final_img = "img/final_img.jpg"
		self.win_img = "img/win_img.jfif"
		self.logo_img = "img/Battleship.png"
		self.last_img = "img/congrats.jfif"
		self.users_path = "users.json"

	def load_data(self, path):
		with open(path, "r") as json_data:
			data = json.load(json_data)
		return data


	def login(self, username, password):
		users = self.load_data(self.users_path)
		if username in users:
			if password == users[username]["password"]:
				return True
			else:
				return False
		else:
			return False