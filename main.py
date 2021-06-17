import tkinter as tk
import time
from tkinter import messagebox as msg

from config import Config
from ship import Ship
from player import Player
from board import Board
from loginPage import LoginPage


class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)

		self.create_container()


		self.pages = {}
		self.create_board()
		self.create_loginPage()
	

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def auth_login(self):
		username = self.pages['loginPage'].var_username.get()
		password = self.pages['loginPage'].var_password.get()

		granted = self.config.login(username, password)
		if granted:
			self.change_page('board')

		self.pages['loginPage'].setToEmptyEntry()


	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_loginPage(self):
		self.pages['loginPage'] = LoginPage(self.container, self)
	


class Game: 

	def __init__(self):
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.windows = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			return True
		return False

	def button_clicked(self, pos_x, pos_y):
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.windows.pages['board'].change_img_button(pos_x, pos_y, win)

		if win:
			confirm = msg.askyesnocancel("Yeay You Win", f"You Find The Ship! at  {pos_x+1},{pos_y+1}\nPress Yes to Exit The Game\nRun this program again to Play it again")
			if confirm:
				exit()
			
	def run(self):
		self.windows.mainloop()


if __name__ == '__main__':
	my_battleship = Game()
	my_battleship.run()