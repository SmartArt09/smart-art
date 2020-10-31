#Import the modules
import random, time, sys

#Define the function
def rand_pass():
	##All possible characters in password
	string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	
	##Print the password heading followed by the password
	while True:
		print('Password:', end = ' ')
		
	##Password printing for the random length as a typewriter		
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
		print()
		break
		
#Function call
rand_pass()