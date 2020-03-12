from operator import itemgetter, attrgetter
from collections import OrderedDict
import collections


class Win:
	#will return the best win condition.
	def win_check(hand):

		#sorts the hand_sorted acording to Card.face_value
		hand.foo_hand = sorted(hand.foo_hand, key=lambda Card : Card.face_value, reverse=True)
		
		#creates a list straight_check, which contains the face_values

		face_lst = [card.face_value for card in hand.foo_hand]
		
		#for card in hand.foo_hand:
			
			#print(card.face_value)

		#bool, int, key 
		win_loop, rank, key, final_hand = Win.is_straight(hand)
		#print('straight ', win_loop, rank, key) #can return here if True
		if win_loop:
			return win_loop, rank, key, final_hand #consider passing the full best hand.	

		#key is returning format => 10 of Hearts
		win_loop, rank, key, final_hand = Win.flush(hand.foo_hand)
		#print('flush ', win_loop, rank, key)
		if win_loop:
			return win_loop, rank, key, final_hand #consider passing the full best hand.

		win_loop, rank, key, final_hand = Win.is_pair(face_lst, hand)
		#print('is_pair ', win_loop, rank, key, '\n') #can return here if true
		if win_loop:
			return win_loop, rank, key, final_hand #consider passing the full best hand.
		else:
			return False, 0, key, final_hand

		
	def is_straight(hand):
	
		my_dict=OrderedDict({ 14 : set([10, 11, 12, 13, 14]),
		
				13 : set([9, 10, 11, 12, 13]),
		
				12 : set([8, 9, 10, 11, 12]),
		
				11 : set([7, 8, 9, 10, 11]),
		
				10 : set([6, 7, 8, 9, 10]),
		
				9 : set([5, 6, 7, 8, 9]),
		
				8 : set([4, 5, 6, 7, 8]),
		
				7 : set([3, 4, 5, 6, 7]),
		
				6 : set([2, 3, 4, 5, 6]),
		
				5 : set([15, 2, 3, 4, 5,])})

		face_lst = [x.face_value for x in hand.foo_hand]
		#list will take multiple hands that are straight.
		mult_straight = []

		#separates multiple straights, check if any is flush.

		#key is the string, item is the set
		for key, item in my_dict.items():
			
			if item.issubset(face_lst):
				#generates a list(hand) with the cards if the cards.face_value is part o item.
				mult_straight.append([card for card in hand.foo_hand if card.face_value in item])

			
			#passes the hand to flush
		for hand in mult_straight:
			win_loop, rank, key, final_hand = Win.flush(hand)
			
			if win_loop:
				return True, 20, key, final_hand
		
		if len(mult_straight) > 0:
			#print('Straight')
			return True, 14, mult_straight[0][-1], None
		else:
			return False, None, 0, None

	def flush(hand):
		

		hand_sorted = hand

		spades_count = [card for card in hand_sorted if card.card_suit == 'Spades']
		hearts_count = [card for card in hand_sorted if card.card_suit == 'Hearts']
		clubs_count = [card for card in hand_sorted if card.card_suit == 'Clubs']
		diamonds_count = [card for card in hand_sorted if card.card_suit == 'Diamonds']

		#
		#only returning 1 value as key, if higher card is the same will be a draw.
		#

		if len(spades_count) >=5:
			return True, 12, [card.face_value for card in spades_count[0:5]], spades_count[0:5]
		#Spade, Hearts, Clubs, Diamonds
		if len(hearts_count)  >= 5:
			return True, 12, [card.face_value for card in hearts_count[0:5]], hearts_count[0:5]
		if len(clubs_count) >= 5:
			return True, 12, [card.face_value for card in clubs_count[0:5]], clubs_count[0:5]
		if len(diamonds_count) >= 5:
			return True, 12, [card.face_value for card in diamonds_count[0:5]], diamonds_count[0:5]
		else:
			return False, None, 0, None

		

	def is_pair(lst1, hand):
		my_lst = lst1
		trio_count=[]
		pairs_count=[]
		#print('inside is pair,', my_lst)

		#print('Mark bug', collections.Counter(my_lst))

		my_counter = collections.Counter(my_lst) 
		#card, occurrences
		for cardface,occurrences in my_counter.items():
			#print('Card, #Occurrences', cardface, occurrences)

			if occurrences == 4:
				final_hand = [card for card in hand.foo_hand if card.face_value == cardface]
				#sorted(lst1, key = lambda Card : Card.face_value, reverse=True)
				for card in hand.foo_hand:
					if card.face_value==cardface:
						pass
					if card.face_value!=cardface:
						final_hand.append(card)
						break

				return True, 18, (cardface, occurrences), final_hand
			if occurrences == 3:
				trio_count.append(cardface)
			if occurrences == 2:
				pairs_count.append(cardface)

		#sorted(trio_count)
		#sorted(pairs_count)		
		#fullhouse
		if ((len(trio_count)>=1 and len(pairs_count)>= 1) or (len(trio_count) > 1)):
			#print('Fullhouse')
		
			trio = trio_count[0]

			#bigger pair
			
			pair = pairs_count[0] if len(pairs_count) >= 1 else None



			if pair == None:
				pair = trio_count[1]

			return True, 16, (trio, pair), None

		
		if len(trio_count) == 1:
			final_hand = [card for card in hand.foo_hand if card == trio_count]
			
			for card in hand.foo_hand[:5]:
				if card.face_value != trio_count:
					final_hand.append(card)
				if len(final_hand)==5:
					break
			##
			##add something to return higher card.	
			##final hand should be returning the correct hand.
			print('Trio!', trio_count)
			return True, 10, trio_count, final_hand

		if len(pairs_count) > 1:
			final_hand=[card for card in hand.foo_hand if (card.face_value == pairs_count[0] or card.face_value == pairs_count[1])]
			
			for card in hand.foo_hand[:7]:
				
					if (card.face_value != pairs_count[0] and card.face_value != pairs_count[1]):
						final_hand.append(card)
						break
					if len(final_hand)==5:
						break

			return True, 8, (hand.foo_hand[0].face_value, hand.foo_hand[1].face_value), final_hand
		if len(pairs_count) == 1:
			final_hand=[card for card in hand.foo_hand if card.face_value == pairs_count[0]]
					
			for card in hand.foo_hand[:7]:
				if card.face_value != pairs_count[0]:
					final_hand.append(card)
					#print('2', card.face_value)
				if len(final_hand)==5:
					break

			return True, 6, pairs_count[-1], final_hand
						
			
		else:
			final_hand=[card for card in hand.foo_hand[0:5]]

			
			return False, 0, 0, final_hand

	