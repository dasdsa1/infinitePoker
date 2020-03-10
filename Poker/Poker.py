from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from subfolder import place_bet
from subfolder import DeckClass
from subfolder import win_check
from subfolder import win_sort
import os
from PIL import ImageTk
from PIL import Image
import random


	
root=Tk()

class hand():
	
	def __init__(self, name=''):
		self.name=name
		self.foo_hand=[]
		self.amount = 1000

	def my_hand():
		return self.foo_hand

	def my_hand_add(self, bar):
		self.foo_hand.append(bar)

	def my_hand_pop(self, element=None):
		if element == None:
			return self.foo_hand.pop()
		else:
			return self.foo_hand.pop(element)

	def my_hand_remove(self, element):
		self.foo_hand.remove(element)

	def shuff(self):
		random.shuffle(self.foo_hand)

	def meld(self, something):
		return self.foo_hand.extend(something)

	def face_val():
		for item in foo_hand:
			return item.face_val
	
	def forget1(self):
		self.foo_hand=[]
		


class player():
	count = 0
	def __init__(self, amount):
		self.amount=amount


player_hand = hand()
house_hand = hand()
table_cards = hand()
my_deck = hand()
npc_hand = hand()
npc2_hand = hand()
control_deck = hand()
control_hand = hand()
possible_hands=[]


class window():

	#setup the inital window:
	def __init__(self, master):
		self.master = master
		master.geometry('1600x900')
		master.title("Poker!")
		master.configure(bg="forest green")

		self.top_label=Label(master, text="Game starting!")

		self.start_button = Button(master, text="Click to Start!", command=start_game)
		self.start_button.grid(column=1,row=1)

		self.card_back = PhotoImage(file='e:\\Poker\\pics\\Capture.png')


		self.table_img = PhotoImage(file='e:\\Poker\\pics\\table_img.png')	
		self.table_label = Label(master, image=self.table_img)
		#self.table_label.grid(column=0, row=1)

		self.restart_button = Button(text='Restart', command=reset_game)
		self.restart_button.grid(column=1, row=4)

		#player_hand
		self.player_hand1 = Label(master)
		self.player_hand2 = Label(master)

		#house_hand
		self.house_hand1 = Label(master)
		self.house_hand2 = Label(master)
		


		#buttons
		self.victory = Button(master, text='Show Down', command=victory)
		

		self.other_button = Button(master, text="Deal", command=deal)
		self.turn_button = Button(master, text="Turn", command=turn)
		self.river_button = Button(master, text="River", command=river)



		#Labels
		self.house_cards_label0 = Label(master)
		self.house_cards_label1 = Label(master)
		self.house_cards_label2 = Label(master)
		self.house_cards_label3 = Label(master)
		self.house_cards_label4 = Label(master)
		self.house_cards_label5 = Label(master)
		self.house_cards_label6 = Label(master)
		self.house_cards_label7 = Label(master)
		self.house_cards_list = [self.house_cards_label0, self.house_cards_label1, self.house_cards_label2, self.house_cards_label3, self.house_cards_label4, self.house_cards_label5, self.house_cards_label6, self.house_cards_label7]
		
		#betting
		self.number_of_runs=Label(master, text='0')
		self.wallet_display=Label(master, text='1000')
		self.number_of_runs.grid(column=0, row=5)
		self.wallet_display.grid(column=1, row=5)

def start_game():
	
	

	poker_gui.start_button.grid_forget()
	
	
	for i in range(1,52):
		my_deck.my_hand_add(DeckClass.Card(i))
		control_deck.my_hand_add(DeckClass.Card(i))

	hand.shuff(my_deck)
	
	player_hand.my_hand_add(my_deck.my_hand_pop())
	house_hand.my_hand_add(my_deck.my_hand_pop())
	player_hand.my_hand_add(my_deck.my_hand_pop())
	house_hand.my_hand_add(my_deck.my_hand_pop())

	#npc_hand.my_hand_add(my_deck.my_hand_pop())
	#npc_hand.my_hand_add(my_deck.my_hand_pop())

	#npc2_hand.my_hand_add(my_deck.my_hand_pop())
	#npc2_hand.my_hand_add(my_deck.my_hand_pop())

	poker_gui.player_hand1.configure(image=player_hand.foo_hand[0].card_image)
	poker_gui.player_hand2.configure(image=player_hand.foo_hand[1].card_image)
	poker_gui.player_hand1.grid(column=1, row=0)
	poker_gui.player_hand2.grid(column=2, row=0)

	poker_gui.house_hand1.configure(image=poker_gui.card_back)
	poker_gui.house_hand2.configure(image=poker_gui.card_back)	
	
	poker_gui.house_hand1.grid(column=1,row=2)
	poker_gui.house_hand2.grid(column=2, row=2)	


	poker_gui.other_button.grid(column=0, row=4)

	

				
#deal
def deal():

	
	#my_deck.my_hand_pop()
	
	table_cards.my_hand_add(my_deck.my_hand_pop())
	table_cards.my_hand_add(my_deck.my_hand_pop())
	table_cards.my_hand_add(my_deck.my_hand_pop())

	for i in range(3):
		poker_gui.house_cards_list[i].configure(image=table_cards.foo_hand[i].card_image)
		poker_gui.house_cards_list[i].grid(column=i+1, row=1)

	poker_gui.other_button.grid_forget()
	poker_gui.turn_button.grid(column=0, row=4)		
	
	control_hand.meld(table_cards.foo_hand)
	control_hand.meld(house_hand.foo_hand)
	
	#receives the list of possible combinations from place_bet
	
	combinations_list = place_bet.place_bet.place_bet(table_cards, control_hand, control_deck)
	#creates a list with the possible hands the player may have.
	possible_hands=[]
	for (card1,card2) in combinations_list:
		possible_hands.append(hand())
		possible_hands[-1].meld(table_cards.foo_hand)
		possible_hands[-1].my_hand_add(card1)
		possible_hands[-1].my_hand_add(card2)

	ranker = place_bet.place_bet.rank_check(possible_hands)

	
def turn():

	
	control_hand.my_hand_add(my_deck.foo_hand[-1])
	table_cards.my_hand_add(my_deck.my_hand_pop())

	poker_gui.house_cards_list[4].configure(image=table_cards.foo_hand[-1].card_image)
	poker_gui.house_cards_list[4].grid(column=5, row=1)

	poker_gui.turn_button.grid_forget()
	poker_gui.river_button.grid(column=0, row=4)
	
	
	place_bet.place_bet.place_bet(table_cards, control_hand, control_deck)
	
	#house_loop, house_rank, house_key, house_final_hand = win_check.Win.win_check(house_hand)
	
	combinations_list = place_bet.place_bet.place_bet(table_cards, control_hand, control_deck)
	#creates a list with the possible hands the player may have.
	possible_hands=[]
	for (card1,card2) in combinations_list:
		possible_hands.append(hand())
		possible_hands[-1].meld(table_cards.foo_hand)
		possible_hands[-1].my_hand_add(card1)
		possible_hands[-1].my_hand_add(card2)

	ranker = place_bet.place_bet.rank_check(possible_hands)
	

def river():

	poker_gui.victory.grid(column=2, row=4)
	control_hand.my_hand_add(my_deck.foo_hand[-1])
	
	
	poker_gui.house_hand1.configure(image=house_hand.foo_hand[0].card_image)
	poker_gui.house_hand2.configure(image=house_hand.foo_hand[1].card_image)
	
	poker_gui.river_button.grid_forget()

	
	table_cards.my_hand_add(my_deck.my_hand_pop())
	poker_gui.house_cards_list[5].configure(image=table_cards.foo_hand[-1].card_image)
	poker_gui.house_cards_list[5].grid(column=6, row=1)

	poker_gui.river_button.grid_forget()

	place_bet.place_bet.place_bet(table_cards, control_hand, control_deck)
	combinations_list = place_bet.place_bet.place_bet(table_cards, control_hand, control_deck)
	#creates a list with the possible hands the player may have.
	possible_hands=[]
	for (card1,card2) in combinations_list:
		possible_hands.append(hand())
		possible_hands[-1].meld(table_cards.foo_hand)
		possible_hands[-1].my_hand_add(card1)
		possible_hands[-1].my_hand_add(card2)

	ranker = place_bet.place_bet.rank_check(possible_hands)
	
	print('end')

def victory():

	player_hand.meld(table_cards.foo_hand)
	house_hand.meld(table_cards.foo_hand)
	player_loop, player_rank, player_key, player_final_hand = win_check.Win.win_check(player_hand)
	house_loop, house_rank, house_key, house_final_hand = win_check.Win.win_check(house_hand)
	win_sort.Win_sort.win_sort(player_loop, player_rank, player_key, house_loop, house_rank, house_key, player_final_hand, house_final_hand)		
	print(player_rank, '\n', house_rank)

def reset_game():

	poker_gui.turn_button.grid_forget()
	poker_gui.river_button.grid_forget()
	poker_gui.other_button.grid(column=0, row=4)
	hand.forget1(player_hand)
	hand.forget1(house_hand)
	hand.forget1(table_cards)
	hand.forget1(my_deck)
	hand.forget1(control_deck)
	hand.forget1(control_hand)
	#hand.forget1(npc_hand)
	#hand.forget1(npc2_hand)
	#forgets grid from table
	for item in poker_gui.house_cards_list:
		item.grid_forget()

	print('\n')
	print('\n')
	print('\n')

	start_game()

poker_gui=window(root)



root.mainloop()