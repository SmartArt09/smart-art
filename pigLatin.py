def pigLatin():
	s = input('Enter a normal string:')
	a = s.split()
	print('The Pig Latin string is: ')
	for i in l:
		i = a[1: ] + a[0] + 'ay'
		print(i, end = ' ')
pigLatin()