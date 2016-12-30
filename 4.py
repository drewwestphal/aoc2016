#!/usr/bin/python
import re



def parseRoom(roomstr):
	pcs = re.findall(r"\w+", roomstr)
	checksum = pcs.pop()
	sector = int(pcs.pop())
	words = pcs
	chars = sum([list(pc) for pc in pcs],[])
	conc = {}
	for char in chars:
		try:
			conc[char] = conc[char]+1
		except KeyError:
			conc[char] = 1
	checksum_computed = ''.join(str(x[0]) for x in sorted(conc.items(), key=lambda x: (-x[1], x[0])))[:5]
	return (words, sector, checksum_computed==checksum)

def rotateN(str, n):
	return ''.join(chr((ord(char)-ord('a')+n)%26+ord('a')) for char in str)	

count = 0
for line in open('./4input.txt'):
	parsed = parseRoom(line)
	count+= parsed[1] if parsed[2] else 0
	print parsed[1], ' '.join([rotateN(x,parsed[1]) for x in parsed[0]])

print count
