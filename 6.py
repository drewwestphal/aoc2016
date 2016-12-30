#!/usr/bin/python

data = open('./6input.txt')


rows = [list(x.strip()) for x in data]
columns = []
for i in range(0,len(rows[0])):
	column = [row[i] for row in rows]
	conc = {}
	for char in column:
		try:
			conc[char] = conc[char]+1
		except KeyError:
			conc[char] = 1
	print [str(x[0]) for x in sorted(conc.items(), key=lambda x: -x[1])][0]+':'+[str(x[0]) for x in sorted(conc.items(), key=lambda x: x[1])][0]

