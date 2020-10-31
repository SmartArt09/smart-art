import random, time, sys

def delay_print(s):
	for i in s:
		sys.stdout.write(i)
		sys.stdout.flush()
		if i != '\n':
			time.sleep(0.05)
		else:
			time.sleep(0.5)

delay_print('')