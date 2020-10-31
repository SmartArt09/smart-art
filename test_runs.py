import random

c = 0
while True:
	x = random.randint(0, 100)
	t = random.randint(0, 100)
	print(t)
	
	if x == t:
		print('The test succeeded!')
		break
	else:
		c += 1
		print('The test failed!')
print('The failed tests count:', c)

if c >= 100:
	print('Remarks: The test run was inefficient.')
if 50 < c < 99:
	print('Remarks: The test run can do better.')
if 20 < c < 50:
	print('Remarks: The test run was efficient.')
if c <= 20:
	print('Remarks: The test run was highly efficient.')