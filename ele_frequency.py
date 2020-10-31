#Import the modules
import random, time

#Initialize variables and generate a random length for the list
l = []
n = random.randint(7, 20)
print('The length of the randomly generated list is:', n, '\n')
time.sleep(1)

#Generate the list of random numbers
x = 0
while True:
	l.append(random.randint(1, 20))
	x += 1
	if x == n:
		break
print('The randomly generated list is:')
print(l, '\n')

#Find the frequencies of all the list elements
print('The frequencies of each element in the list:\n')
time.sleep(1)
d = {}
for i in l:
	d[i] = l.count(i)
for a in d:
	print('{} ---> {} time(s)'.format(a, d[a]))