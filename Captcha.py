#Import the modules
import random, time, sys

#Define the function
def captcha():
	##All possible characters in captcha
	string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	
	##Print the captcha heading followed by the captcha
	while True:
		print('Captcha:', end = ' ')
		
	##Captcha printing for the random length as a typewriter		
		a = []
		for i in range(random.randint(6, 8)):
			x = random.choice(string)
			a.append(x)
			l = ''.join(a)
			for i in x:
				sys.stdout.write(x)
				sys.stdout.flush()
				if i != '\n':
				 	time.sleep(0.1)		 	
		time.sleep(1)
	
	##Captcha input and checking whether the captcha entered is correct or not
		c = input('\nEnter the above captcha: ')
		if len(c) <= 0:
			print('Please enter something...\n')
		else:
			if c == l:
				print('Correct captcha!')
				break
			else:
				print('Wrong captcha!\n')

#Function call
captcha()