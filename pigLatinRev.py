def pigLatinRev():
	s = input('Enter a string in Pig Latin:')
	a = s.split()
	print('The normal string is: ')
	for i in a:
		x = i[-3] + i[ : -3] 
		print(x, end = ' ')
pigLatinRev()