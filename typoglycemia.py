import string
from itertools import permutations

# lowercase letters
lst = string.ascii_lowercase

# English dictionary named "dict"
diccionario = open("dict", "r")

alphabetical = []

prev = "a"

toadd = []

for word in diccionario:
	curr = word.lower()
	curr = curr[:len(curr) - 1]
	if curr[0] == prev[0]:
		toadd.append(curr)
	else:
		alphabetical.append(toadd)
		toadd = []
	prev = curr

alphabetical.append(toadd)

for l in alphabetical:
	l.sort(key=len)

prev = "four"

alphLen = []

toadd = []

for l in alphabetical:
	for x in l:
		if len(x) > 3:
			if len(x) == len(prev):
				toadd.append(x)
			else:
				alphLen.append(toadd)
				toadd = []
			prev = x

alphLen.append(toadd)

for l in alphLen:
	for i in range(len(l)):
		l[i] = l[i][::-1]

for l in alphLen:
	l.sort()

alphLenLast = []

prev = "a"

toadd = []

for l in alphLen:
	for x in l:
		if x[0] == prev[0]:
			toadd.append(x)
			# toadd.append(x)
		else:
			alphLenLast.append(toadd)
			toadd = []
		prev = x

alphLenLast.append(toadd)

for l in alphLenLast:
	for x in range(len(l)):
		l[x] = l[x][::-1]

breakCambridge = []

for l in alphLenLast:
	skip = []
	for i in l:
		# http://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
		perms = [''.join(p) for p in permutations(i)]
		for p in perms:
			for x in l:
				if p not in skip and i != x and p == x:
					skip.append(x);
					skip.append(i);
					breakCambridge.append((i, x))
					print(breakCambridge[0])



		


