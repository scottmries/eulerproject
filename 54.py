with open("poker_hands.txt") as f:
    content = f.readlines()

values_order = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
hands_order = ["HC","P","2P","3","S","F","FH","4","SF"]

player1_hands = 0
player2_hands = 0



# Just write functions to check Royal Flush, Straight Flush, Four of a Kind, Full House, Flush, Straight, 3-of-a-kind, 2 pair, 1 pair, High card, returning appropriate qualities like highs card in a flush, straight, multiples, or high card
# Write functions to check flush, straight, pair, three- and four-of a kind, then combine
# Royal Flush returns nothing
# Straight Flush returns high card
# Four of a kind returns card
# Full House returns card of trips
# Flush returns three high cards
# Straight returns high card
# Three of a kind returns the card
# Two pair returns the cards of the pairs and the fifth card
# One pair returns the card of the pair and the three cards
# High card returns the whole hand

# PASS ALL THESE FUNCTIONS SUITS, VALUES

def is_flush(suits, values):
	if (len(set(suits))==1):
		print "flush", suits, values
	return (len(set(suits))==1,sorted(values))

	# return len(set([c[1] for c in cards]))==1

def is_straight(suits, values):
	global values_order
	v = sorted([values_order.index(c[0]) for c in values])
	if len(set(values))==len(values):
		if abs(v[0]-v[-1])==4:
			print "straight", suits, values
			return (True,values[-1])
			
		else:
			return (False,values[-1])
	else:
		return (False, values[-1])

def has_multiples(suits,values):
	# Return a tuple with (which_multiple,list_of_values)
	dupes = list()
	uniqs = list()
	for v in values:
		if v not in uniqs:
			uniqs.append(v)
		else:
			dupes.append(v)
	if len(uniqs) == 2:
		if len(set(dupes))==1:
			# there's a four of a kind and its value is dupes[0]
			return (4,dupes[0])
		else:
			trips = max(set(dupes), key=dupes.count)
			dupes = filter(lambda a: a != trips, dupes)
			# there's a full house, return its high value first and its low second
			return ("full",trips,dupes[0])
	elif len(uniqs) == 3:
		# could be two pair or trips
		if len(set(dupes))==1:
			return (3,dupes[0])
		else:
			return("two pair",max(dupes),min(dupes))
	elif len(uniqs) == 4:
		# pair
		return(2,dupes[0],sorted(uniqs))
	else:
		# high card
		return(sorted(uniqs))



def get_hand(suits,values):
	flush = is_flush(suits,values)
	straight = is_straight(suits,values)
	multiples = has_multiples(suits,values)
	values_indices = [values_order.index(v) for v in values]
	sorted_values = [values_order[v] for v in sorted(values_indices)]
	# print flush, straight, multiples
	# generate a list of hand ranks (in hex?)
	if flush[0] and straight[0]:
		return ("SF",max(values))
	elif multiples[0] == 4:
		return ("4",multiples[1])
	elif multiples[0] == "full":
		return ("FH",multiples[1])
	elif flush[0]:
		return ("F", sorted_values[-1],sorted_values[-2],sorted_values[-3],sorted_values[-4],sorted_values[-5])
	elif straight[0]:
		return ("S",max(values))
	elif multiples[0] == 3:
		return ("3",multiples[1])
	elif multiples[0] == "two pair":
		if values_order.index(multiples[1])>values_order.index(multiples[2]):
			return ("2P",multiples[1],multiples[2])
		else:
			return ("2P",multiples[2],multiples[1])
	elif multiples[0] == 2:
		return ("P",multiples[1])
	else: return ("HC",sorted_values[-1],sorted_values[-2],sorted_values[-3],sorted_values[-4],sorted_values[-5])

def compare_hands(hand1,hand2):
	global player1_hands, player2_hands
	if hands_order.index(hand1[0])>hands_order.index(hand2[0]):
		player1_hands+=1

	elif hands_order.index(hand1[0])==hands_order.index(hand2[0]):
		
		i = 1
		while True:
			if i == len(hand1):
				break
			if values_order.index(hand1[i]) > values_order.index(hand2[i]):
				player1_hands+=1
				break
			elif values_order.index(hand1[i]) < values_order.index(hand2[i]):
				player2_hands+=1
				break
			else:
				print player1_hands, player2_hands
				i+=1
	else:
		player2_hands+=1
		
		return False




for e,c in enumerate(content):

	p1 = c[:14]
	p2 = c[15:]
	# print e, p1, p2
	# p1 = "5H 5C 6S 7S KD"
	# p2 = "2C 3S 8S 8D TD"
	p1_suits = list()
	p1_values = list()
	p2_suits = list()
	p2_values = list()
	for i in range(0,5):
		p1_values.append(p1[3*i])
		p1_suits.append(p1[3*i+1])
		p2_values.append(p2[3*i])
		p2_suits.append(p2[3*i+1])
	p1_hand = get_hand(p1_suits,p1_values)
	p2_hand = get_hand(p2_suits,p2_values)
	# print p1_hand, p2_hand
	compare_hands(p1_hand,p2_hand)

print player1_hands,player2_hands
