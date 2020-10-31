from typewriter import delay_print as dp
import time, os

def login():
	d = {}
	while True:
		user = input('Enter your username: ')
		if (0 <= len(user) <= 4):
			print('Please enter a valid username.\n')
		else:
			break
	while True:
		passwd = input('\nEnter a strong password: ')
		if len(passwd) < 6:
			print('Sorry! The password is too short.\n')
			ch = input('Do you want to generate a random password?(Y/y/N/n): ')
			if ch == 'y' or ch == 'Y':
				dp('\nGenerating a random password, please wait....\n')
				time.sleep(0.5)
				from passwordGen import rand_pass
				dp('\nPassword generated successfully!\n')
				d[user] = passwd
				print('Password saved!\n')
				from Captcha import captcha
				time.sleep(1)
				os.system('clear')
				break
			elif ch == 'n' or ch == 'N':
				print('Please input again!')
				pass
			else:
				print('Sorry that was not an option!')
		else:
			d[user] = passwd
			print('Password saved!\n')
			from Captcha import captcha
			time.sleep(1)
			os.system('clear')
			break
login()