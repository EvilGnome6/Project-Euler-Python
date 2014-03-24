#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

#    High Card: Highest value card.
#    One Pair: Two cards of the same value.
#    Two Pairs: Two different pairs.
#    Three of a Kind: Three cards of the same value.
#    Straight: All cards are consecutive values.
#    Flush: All cards of the same suit.
#    Full House: Three of a kind and a pair.
#    Four of a Kind: Four cards of the same value.
#    Straight Flush: All cards are consecutive values of same suit.
#    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

#The cards are valued in the order:
#2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

#Consider the following five hands dealt to two players:
#Hand	 	Player 1	 	Player 2	 		Winner
#1	 	5H 5C 6S 7S KD		2C 3S 8S 8D TD		Player 2
#		Pair of Fives		Pair of Eights		
	 	
#2	 	5D 8C 9S JS AC		2C 5C 7D 8S QH
#		Highest card Ace	Highest card Queen	Player 1
	 	
#3	 	2D 9C AS AH AC		3D 6D 7D TD QD
#		Three Aces			Flush with Diamonds	Player 2

#4	 	4D 6S 9H QH QC		3D 6D 7H QD QS
#		Pair of Queens		Pair of Queens
#		Highest card Nine	Highest card Seven	Player 1
	 	
#5	 	2H 2D 4C 4D 4S		3C 3D 3S 9S 9D
#		Full House			Full House
#		With Three Fours	with Three Threes	Player 1

#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

#How many hands does Player 1 win?

pokerfile = open("poker.txt")
deals = []

while True:
	line = pokerfile.readline()
	if line == "": break
	else: deals.append(pokerfile.readline())

pokerfile.close()

def getscore(deal):
	cards = []
	score = [0]*10
	for i in range(0, 5):
		number = deal[i*3]
		if number == "T": cards.append([10])
		elif number == "J": cards.append([11])
		elif number == "Q": cards.append([12])
		elif number == "K": cards.append([13])
		elif number == "A": cards.append([14])
		else: cards.append([int(number)])
		suit = deal[i*3+1]
		if suit == "C": cards[i].append(1)
		if suit == "D": cards[i].append(2)
		if suit == "H": cards[i].append(3)
		if suit == "S": cards[i].append(4)
	print deal, cards
	
	#create lists of values and list of suits of the cards
	values = []
	suits = []
	for i in range(0, 5):
		values.append(cards[i][0])
		suits.append(cards[i][1])
	
	#High Card: Highest value card.
	score[9] = max(values)
	
	#One Pair: Two cards of the same value.
	pair = 0
	for i in range(2, 15):
		if values.count(i) == 2:
			if i > pair: pair = i
	score[8] = pair
	
	#Two Pairs: Two different pairs.
	pair = 0
	for i in range(2, 15):
		if values.count(i) == 2:
			pair = i
			for j in range(i+1, 15):
				if values.count(j) == 2:
					pair += j
					score[7] = pair
			break
			
	#Three of a Kind: Three cards of the same value.
	for i in range(2, 15):
		if values.count(i) == 3: score[6] = i
	
	#Straight: All cards are consecutive values.
	streak = 0
	for i in range(2, 15):
		if streak == 5: break
		if values.count(i) == 1:
			streak = 1
			for j in range(i+1, i+5):
				if values.count(j) == 1:
					streak += 1
					if streak == 5: score[5] = j
				else: break
	
	#Flush: All cards of the same suit.
	flush = True
	for i in range(0, 4):
		if suits[i] != suits[i+1]: flush = False
	if flush == True: score[4] = 1
	
	#Full House: Three of a kind and a pair.
	if score[8] > 0 and score[9] > 0: score[3] = 1
	
	#Four of a Kind: Four cards of the same value.
	for i in range(2, 15):
		if values.count(i) == 4: score[2] = i
		
	#Straight Flush: All cards are consecutive values of same suit.
	if score[4] > 0 and score[5] > 0: score[1] = 1
	
	#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
	if score[1] == 1 and score[5] == 14: score[0] = 1
	
	return score
	
print getscore(deals[0][0:14])
print getscore(deals[0][15:29])
print getscore("TC JC QC KC AC")