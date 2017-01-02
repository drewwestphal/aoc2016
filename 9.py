#!/usr/bin/python

import re
from time import sleep

class cblock: 

	RE_MARKER = r'\((\d+)x(\d+)\)'
	
	def __init__(self, content, maxDepth=1, curDepth=0, nrepeat=1):
		self.content = content
		self.nRepetitions = nrepeat
		self.curDepth = curDepth
		self.maxDepth = maxDepth
		print('consing blk', self.content, maxDepth, curDepth, nrepeat)
		
	def getChildren(self):
		if self.curDepth==self.maxDepth or not re.findall(cblock.RE_MARKER,self.content):
			return []
		else:
			content = self.content
			children = []
			while content:
				fb = cblock.firstBlock(content, self.curDepth, self.maxDepth)
				children.append(fb[0])
				content = fb[1]
			return children
	
	def blockLen(self):
		if self.getChildren():
			return sum([child.blockLen() for child in self.getChildren()])*self.nRepetitions
		else:
			return len(self.content)*self.nRepetitions
			

	@staticmethod
	def firstBlock(content, curDepth, maxDepth):
		match = re.search(cblock.RE_MARKER, content)
		nRepeat = 1
		blockContent = ''.join(content.split())
		remainingContent = ''
		if match:
			if match.start(0)==0:
				lenRepeat = int(match.group(1))
				nRepeat = int(match.group(2))
				blockContent = content[match.end(0):match.end(0)+lenRepeat]
				remainingContent = content[match.end(0)+lenRepeat:]
			else:
				blockContent = content[:match.start(0)]
				remainingContent = content[match.start(0):]

		return (cblock(blockContent,maxDepth,curDepth+1,nRepeat),remainingContent)
			

## tests 
print cblock('ADVENT').blockLen()
print cblock('A(1x5)BC').blockLen()
print cblock('(3x3)XYZ').blockLen()
print cblock('A(2x2)BCD(2x2)EFG').blockLen()
print cblock('(6x1)(1x3)A').blockLen()
print cblock('X(8x2)(3x3)ABCY').blockLen()


print cblock('(3x3)XYZ',-1).blockLen()
print cblock('X(8x2)(3x3)ABCY',-1).blockLen()
print cblock('(27x12)(20x12)(13x14)(7x10)(1x12)A',-1).blockLen()
print cblock('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN',-1).blockLen()



with open('9input.txt') as file:
	ct = file.read()
	comp = cblock(ct)
	comp2 = cblock(ct, -1)
	print comp.blockLen()
	print comp2.blockLen()