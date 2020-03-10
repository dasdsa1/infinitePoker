import random
from itertools import combinations
from collections import Counter
from . import win_check


class place_bet:

	def place_bet(table_hand, house_hand, control_deck):

		#removes the cards from the 
		for control_card in control_deck.foo_hand:
			for house_card in house_hand.foo_hand:
				if control_card.card_number == house_card.card_number:
					#print(control_card.card_number)
					control_deck.my_hand_remove(control_card)

		#creates a list with tuples, with the combinations on the deck (left over cards)
		combinations_list = list(combinations(control_deck.foo_hand, 2))
		
		return combinations_list
		
	def rank_check(possible_hands):
		#import win_check.Win as win
		#creates a list with the 
		rank_count =[]
		for hand in possible_hands:

			possible_loop, possible_rank, possible_key, possible_final_hand = win_check.Win.win_check(hand)
			rank_count.append(possible_rank)

	
		rank_counter = Counter(rank_count)
		#cardface, occurrences
		ranker = rank_counter.most_common()[:-4-1:-1]
	


		for cardface,occurrences in rank_counter.items():
				print('in Deal Card, #Occurrences', cardface, occurrences)
		
		
		
		rank_sum = 0
		occur_sum = 0
		for rank,occur in ranker:
			rank_sum += rank
			occur_sum += occur


		print((rank_sum/4)+random.randint(-2,2))



		print(ranker)

		#return ranker


		#receives the house_hand and player_hand
		#generates a list with all possible ranks from player_hand
		#generates a list with all possible ranks from house_hand
		#if average player_ranks+-random < house_hand_rank-range, bet accepted.
		return ranker