from operator import itemgetter, attrgetter
from collections import OrderedDict
import collections

from tkinter import messagebox

class Win_sort:

	def win_sort(player_loop, player_rank, player_key, house_loop, house_rank, house_key, player_final_hand, house_final_hand):

		player_rank_name = Win_sort.rank_name(player_rank)
		house_rank_name = Win_sort.rank_name(house_rank)

		


		if player_rank > house_rank:
			messagebox.showinfo(message='1Player won with the score of {}.'.format(player_rank_name))
			return 'Player', player_rank, player_key
		if player_rank < house_rank:
			messagebox.showinfo(message='2House won with the score of {}.'.format(house_rank_name))
			return 'House', house_rank, house_key
		else:
				
			if player_key > house_key:
				messagebox.showinfo(message='3Player won a tie with {}.'.format(player_rank_name))
				return 'Player', player_rank, player_key
			if player_key < house_key:
				messagebox.showinfo(message='4House won a tie Rank {}.'.format(house_rank_name))
				return 'House', house_rank, player_key
			if player_final_hand == None:
				messagebox.showinfo(message='It\'s a draw, Rank {}.'.format(player_rank_name))
				return None, player_rank, player_key	
			elif player_key == house_key:

					for player_card,house_card in zip(player_final_hand[0:5], house_final_hand[0:5]):
						
						
						if player_card.face_value > house_card.face_value:
							messagebox.showinfo(message='5Player won a tie: {}, kicker: {}'.format(player_rank_name, player_card.face_value))
							return 'Player', player_rank, player_card.card_number
						if player_card.face_value < house_card.face_value:
							messagebox.showinfo(message='6Player lost a tie: Rank {}, kicker: {}'.format(player_rank_name, house_card.face_value))
							return 'House', player_rank, house_card.card_number
			
			else:
				messagebox.showinfo(message='It\'s a draw!')
				return None, player_rank, player_key	
			
						

					# change so player_hand will come from win_check along with the house hand, with the cards in it.
					# currently the algorithm sorts all 7 cards in case of a draw, not only the ones in the win condition hand. - not sure if correct.
					#

					#sorted(player_final_hand, reverse=True, key = lambda Card : Card.face_value)
					#sorted(house_final_hand, reverse=True, key = lambda Card : Card.face_value)
			
	#could also be done by receiving one aditional argument from wincheck, which according to the state would return the string.
	def rank_name(rank):
		if rank == 20:
			return 'Straigh Flush'
		if rank == 18:
			return 'Four Cards'
		if rank == 16:
			return 'Full House'
		if rank == 14:
			return 'Straigh'
		if rank == 12:
			return 'Flush'
		if rank == 10:
			return 'Trio'
		if rank == 8:
			return 'Two Pairs, '
		if rank == 6:
			return 'Pair'
		else:
			return 'Card High'
	

							
			