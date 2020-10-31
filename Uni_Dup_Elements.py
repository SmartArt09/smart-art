def uni_dup(l):
	dup = list(set(l))
	d = {}
	for i in l:
		d[i] = l.count(i)
		if d[i] > 1:
			d.pop(i)
	uni = list(d.keys())
	for i in uni:
		if i in dup:
			dup.remove(i)
	print('Original list: ', l)
	print('List of Unique elements: ', uni)
	print('List of Duplicate elements: ', dup)
uni_dup([1, 3, 2, 1, 4, 5, 6, 6, 2])