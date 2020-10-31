import random

loss_count = 0
while True:
	a = random.randint(0, 10)
	b = random.randint(0, 10)
	c = random.randint(0, 10)
	blackjack = [a, b, c]						
	print(blackjack)
	
	if a == b == c == 7:
		print('Congratulations! You won the blackjack!')
		break
	elif a == b == c == 5:
		print('Congrats! You found the extra pattern!')
		break
	elif a == b == c == 6:
		print("You Illuminati bruh! I'm not playing with ya! Get out!")
		break
	else:
		loss_count += 1
		print('Sorry, you lost!\n')

print('You won after', loss_count, 'tries.')