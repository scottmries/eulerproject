with open("poker_hands.txt") as f:
    content = f.readlines()

values_order = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]



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
	return (len(set(suits))==1,sorted(values))
	# return len(set([c[1] for c in cards]))==1

def is_straight(suits, values):
	global values_order
	v = sorted([values_order.index(c[0]) for c in values])
	if abs(v[0]-v[-1])==4:
		return (True,values[-1])
	else:
		return (False,values[-1])

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
			trips = [max(x) for x in dupes.count(x)](0)
			pair = [dupes.remove(x)](0)
			# there's a full house, return its high value first and its low second
			return ("full",trips,pair)
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

hands_order = ["HC","P","2P","3","S","F","FH","4","SF"]

def get_hand(suits,values):
	flush = is_flush(suits,values)
	straight = is_straight(suits,values)
	multiples = has_multiples(suits,values)
	# print flush, straight, multiples
	# generate a list of hand ranks (in hex?)
	if flush[0] and straight[0]:
		return ("SF",max(values))
	if multiples[0] == 4:
		return ("4",multiples[1])
	if multiples[0] == 
	Royal Flush = Straight Flush with Ace high
	Four of a kind, value
	Full house, value
	Flush, highest cards
	Straight, high card
	Three of a kind, value
	Two pair, values
	Pair, value, high cards
	High card, high cards
	return (flush, straight, multiples)

def compare_hands(hand1,hand2):
	if hand1[0][0] and ha




for c in content:
	# p1 = c[:14]
	# p2 = c[15:]
	p1 = "5H 5C 6S 7S KD"
	p2 = "2C 3S 8S 8D TD"
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
	print p1_hand,p2_hand
