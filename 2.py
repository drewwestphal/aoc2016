#!/usr/bin/python

import string,urllib2


class dialer:

	def __init__(self):
		self.number = 5

	def doDown(self):
		if self.number < 7:
			self.number+=3
		
	def doUp(self):
		if self.number > 3:
			self.number-=3
	
	def doRight(self):
		if self.number%3!=0:
			self.number+=1
	
	def doLeft(self):
		if self.number%3!=1:
			self.number-=1

	def doLine(self, line):
		for char in line: 
			if char == 'U':
				self.doUp()
			if char == 'D':
				self.doDown()
			if char == 'L':
				self.doLeft()
			if char == 'R':
				self.doRight()
		
		print self.number
		

class array_mapper:

	def __init__(self, rows, starting_position, nullchar='\0'):
		self.rows = rows
		self.nullchar = nullchar
		self.position = starting_position
	
	def checkPosition(self,position):
		x = position[0]
		y = position[1]
		
		if x < 0 or y < 0:
			return self.nullchar
		
		try:
			return self.rows[y][x]
		except IndexError:
			return self.nullchar

		
	def move(self,position):
		if self.checkPosition(position)!=self.nullchar:
			self.position=position

	
	def doLine(self, line):
		for char in line:
			if char == 'U':
				self.move((self.position[0], self.position[1]-1))
			if char == 'D':
				self.move((self.position[0], self.position[1]+1))
			if char == 'L':
				self.move((self.position[0]-1, self.position[1]))
			if char == 'R':
				self.move((self.position[0]+1, self.position[1]))
		
		print self.checkPosition(self.position)


dialer = dialer()


mapper = array_mapper([
[0,0,1],
[0,2,3,4],
[5,6,7,8,9],
[0,'A','B','C'],
[0,0,'D']
], (0,2), 0)
				
for line in open('./2input.txt'):
	print '['+line.strip()+']'
	#dialer.doLine(line)
	mapper.doLine(line)
	

