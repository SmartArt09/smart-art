from typewriter import delay_print as dp

def digiLogic():
	print('Welcome to Decimal Converter!')
	
	def dec_to_bin():
		n = int(input('Enter a decimal number:'))
		x = bin(n).replace('0b', '')
		print('Decimal {} in binary form: {}\n'.format(n, x))
		
	def dec_to_oct():
		n = int(input('Enter a decimal number:'))
		x = oct(n).replace('0o', '')
		print('Decimal {} in octal form: {}\n'.format(n, x))
		
	def dec_to_hex():
		n = int(input('Enter a decimal number:'))
		x = hex(n).replace('0x', '')
		print('Decimal {} in hexadecimal form: {}\n'.format(n, x))
	
	def bin_to_dec():
		n = int(input('Enter a combination of binary bits(1\'s & 0\'s):'))
		x = int(str(n), 2)
		print('Binary {} in decimal form: {}\n'.format(n, x))
	
	def oct_to_dec():
		n = int(input('Enter an octal number:'))
		x = int(str(n), 8)
		print('Octal {} in decimal form: {}\n'.format(n, x))
	
	def hex_to_dec():
		n = input('Enter a hexadecimal number:')
		x = int(n, 16)
		print('Hexadecimal {} in decimal form: {}\n'.format(n, x))
	
	def out_choice():
		print('\n1. Decimal to Binary')
		print('2. Decimal to Octal')
		print('3. Decimal to Hexadecimal')
		print('4. Binary to Decimal')
		print('5. Octal to Decimal')
		print('6. Hexadecimal to Decimal')
		print('7. Exit\n')
		ch = int(input('What convertion do you want to perform?(1/2/3/4/5/6/7): '))
		
		if ch == 1:
			print()
			dec_to_bin()
		elif ch == 2:
			print()
			dec_to_oct()
		elif ch == 3:
			print()
			dec_to_hex()
		elif ch == 4:
			print()
			bin_to_dec()
		elif ch == 5:
			print()
			oct_to_dec()
		elif ch == 6:
			print()
			hex_to_dec()
		elif ch == 7:
			print('\nThank you for using our converter!')
			exit()
		else:
			print('\nSorry, please try again!')
		
		print('Do you want to continue?(y/Y/n/N)')
		a = input('Enter your choice: ')
		print()
		if a == 'y' or a == 'Y':
		    pass
		elif a == 'n' or a == 'N':
		    print('Thank you for using our converter!')
		    exit()
		else:
			dp('Sorry, wrong input entered! Continuing program...\n')
	
	while True:
		out_choice()
digiLogic()