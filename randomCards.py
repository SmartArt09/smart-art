#Import the random module
import random, time

#Create the lists of numbers(non-suites) and suites
n_suites = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suites = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

#Shuffle the non-suite list to get a randomly generated series of numbers
random.shuffle(n_suites)

#The main loop randomly iterate through tht lists
print('Some randomly generated card(s) are: \n')
for i in range(random.randint(1, len(n_suites)-1)):
	y = random.randint(0, len(suites)-1)

#Set the name cards
	if n_suites[i] == 1:
		n_suites[i] = 'Ace'
	if n_suites[i] == 11:
		n_suites[i] = 'Jack'
	if n_suites[i] == 12:
		n_suites[i] = 'Queen'
	if n_suites[i] == 13:
		n_suites[i] = 'King'

#Print the cards
	time.sleep(0.05)
	print(n_suites[i], 'of', suites[y])