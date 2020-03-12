from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
from PIL import ImageTk
from PIL import Image
import random


A_number = 0
card_sum = 0


class Card:
	

	#When called, creates a card with a number and a suit.

	#card_value - A to K, string
	#card_face - 2 to 10, A being 'A'
	def __init__(self, card_number):
		self.card_number = card_number
		self.face_value = ''
		self.card_value = '' 
		
		if self.card_number in range(1, 14):
			self.card_suit = 'Spades'
			if self.card_number == 1:
				self.card_value = 'A'
				self.face_value = 14
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Aspade.png')

			elif self.card_number in range(2, 11):
				self.card_value = self.card_number
				self.face_value = self.card_number
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\{}spade.png'.format(self.card_value))
			elif self.card_number == 11:
				self.card_value = 'J'
				self.face_value = 11
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Jspade.png')
			elif self.card_number == 12:
				self.card_value = 'Q'
				self.face_value = 12
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Qspade.png')
			elif self.card_number == 13:
				self.card_value = 'K'
				self.face_value = 13
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Kspade.png')

		elif self.card_number in range(14, 27):
			self.card_suit = 'Hearts'
			if self.card_number == 14:
				self.card_value = 'A'
				self.face_value = 14
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Aheart.png')
			elif self.card_number in range(15, 24):
				self.card_value = self.card_number-13
				self.face_value = self.card_number-13	
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\{}heart.png'.format(self.card_value))
			elif self.card_number == 24:
				self.card_value = 'J'
				self.face_value = 11
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Jheart.png')
			elif self.card_number == 25:
				self.card_value = 'Q'
				self.face_value = 12
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Qheart.png')
			elif self.card_number == 26:
				self.card_value = 'K'
				self.face_value = 13
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Kheart.png')

		elif self.card_number in range(27, 40):
			self.card_suit = 'Clubs'
			if self.card_number == 27:
				self.card_value = 'A'
				self.face_value = 14
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Aclub.png')
			elif self.card_number in range(28, 37):
				self.card_value = self.card_number-26
				self.face_value = self.card_number-26
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\{}club.png'.format(self.card_value))
			elif self.card_number == 37:
				self.card_value = 'J'
				self.face_value = 11
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Jclub.png')
			elif self.card_number == 38:
				self.card_value = 'Q'
				self.face_value = 12
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Qclub.png')
			elif self.card_number == 39:
				self.card_value = 'K'
				self.face_value = 13
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Kclub.png')

		elif self.card_number in range(40, 53):
			self.card_suit = 'Diamonds'
			if self.card_number == 40:
				self.card_value = 'A'
				self.face_value = 14
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Agold.png')
			elif self.card_number in range(41, 50):
				self.card_value = self.card_number-39
				self.face_value = self.card_number-39
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\{}gold.png'.format(self.card_value))
			elif self.card_number == 50:
				self.card_value = 'J'
				self.face_value = 11
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Jgold.png')
			elif self.card_number == 51:
				self.card_value = 'Q'
				self.face_value = 12
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Qgold.png')
			elif self.card_number == 52:
				self.card_value = 'K'
				self.face_value = 13
				self.card_image = PhotoImage(file='e:\\Poker\\pics\\Kgold.png')
		else:
			print(f"{self.card_number} was not assigned any card suit or card value.")
			pass

	def __str__(self):
		try:
			return  f"{self.card_value} of {self.card_suit}"
		except:
			return f"The card is {self.card_number}, no suit or no value was assigned."

		else:
			print("something went wrong")

	
	#def card_number(self):
		#return self.card_number

	#returns the card value. 'J' for example
	#def card_values(self):
		#return self.card_value

	#returns face_value
	#def face_value(self):
		#return self.face_value

	#def card_image(self):
		#return self.card_image

	#def card_suite(self):
		#return self.card_suit