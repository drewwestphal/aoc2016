#!/usr/bin/python
from collections import deque
import re

class modernDisplay: 
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.rows = [[0]*self.width for i in range(0,self.height)]

	def printScreen(self):
		print '\n'.join([''.join(['.' if i==0 else '#' for i in row]) for row in self.rows])
	
	def rectOp(self, width, height):
		self.rows = [[1 if width>idx else px for idx, px in enumerate(row)] if idx<height else row for idx, row in enumerate(self.rows)]

	def rotateRowOp(self,rowIdx,byAmount):
		rotated = deque(self.rows[rowIdx])
		rotated.rotate(byAmount)
		self.rows[rowIdx] = list(rotated)
		
	def rotateColumnOp(self,colIdx,byAmount):
		# zip groups by column...
		# so we do it an undo it to reuse our row rotation shit
		self.rows = zip(*self.rows)
		self.rotateRowOp(colIdx,byAmount)
		self.rows = zip(*self.rows)
		
	def countOnPixels(self):
		return sum([sum(row) for row in self.rows])


		
## tests 
test = modernDisplay(7,3)
test.printScreen()
print '0000000'
test.rectOp(3,2)
test.printScreen()
print '0000000'
test.rotateColumnOp(1,1)
test.printScreen()
print '0000000'
test.rotateRowOp(0,4)
test.printScreen()
print '0000000'
test.rotateColumnOp(1,1)
test.printScreen()
print '0000000'
print '0000000'

data = open('./8input.txt')

display = modernDisplay(50,6)
iter = 0
for line in data: 
#	print '[%s]'%line
	rectCmd = re.match(r'^rect (\d+)x(\d+)', line)
	if rectCmd:
		display.rectOp(int(rectCmd.group(1)),int(rectCmd.group(2)))
		continue

	rotateCmd = re.match(r'^rotate (row|column) (y|x)=(\d+) by (\d+)', line)
	if(rotateCmd.group(1)=='row'):
		display.rotateRowOp(int(rotateCmd.group(3)),int(rotateCmd.group(4)))
	else:
		display.rotateColumnOp(int(rotateCmd.group(3)),int(rotateCmd.group(4)))
		
	#print 'iter %d ---------------------------------\n---------------------' % iter
	#display.printScreen()
	#iter+=1

display.printScreen()
print display.countOnPixels()