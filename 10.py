#!/usr/bin/python

import re

class NumberedThing(object):
	INST_MAP = {}
	
	def __init__(self, number_label):
		self.number_label = number_label
		NumberedThing.INST_MAP.setdefault(self.__class__.__name__,{}).update({self.number():self})

	def number(self):
		return self.number_label
		
	@classmethod
	def getInst(cls, inst_number):
		gotten = NumberedThing.INST_MAP.get(cls.__name__, {}).get(inst_number,None)
		if gotten: return gotten
		return cls(inst_number)

class ChipHolder(NumberedThing):
	def __init__(self, number_label):
		self.chips = []
		super(ChipHolder,self).__init__(number_label)

	def receiveChip(self,chip):
		self.chips.append(chip)

	def __repr__(self):
		return '%s %d has %d chips=%s' % (self.__class__.__name__, self.number(), len(self.chips), self.chips)


class Bot(ChipHolder):
	COMP_TRAIL = {}
	
	def __init__(self, botnumber):
		self.chips = []
		self.give_low = None
		self.give_high = None
		super(self.__class__,self).__init__(botnumber)
			
	def receiveChip(self,chip):
		super(self.__class__,self).receiveChip(chip)
		self.compareChips()
	
	def setLowHigh(self, low, high):
		self.give_low = low
		self.give_high = high
		self.compareChips()
	
	def compareChips(self):
		if len(self.chips)>1 and self.give_low and self.give_high:
			low_chip, high_chip = sorted(self.chips, key=lambda chip: chip.number())
			Bot.COMP_TRAIL[(low_chip.number(), high_chip.number())]=self
			self.give_low.receiveChip(low_chip)
			self.give_high.receiveChip(high_chip)
			self.chips = []
		
	def __repr__(self):
		return '%s; low:%s/high:%s' % (super(self.__class__,self).__repr__(),
		 '%s%d'%(self.give_low.__class__.__name__[:1],self.give_low.number()) if self.give_low else None,
		 '%s%d'%(self.give_high.__class__.__name__[:1],self.give_high.number()) if self.give_high else None)

class Output(ChipHolder): 
	def __init__(self, number):
		super(self.__class__,self).__init__(number)


class Chip(NumberedThing): 
	def __init__(self, chipnumber):
		super(self.__class__,self).__init__(chipnumber)
	
	def __repr__(self):
		return '|chip:%d|' % (self.number())


def parseLine(line):
	match = re.match(r'value (\d+) goes to bot (\d+)',line)
	if match :
		chipnumber, botnumber = [int(i) for i in match.groups()]
		chip = Chip.getInst(chipnumber)
		bot = Bot.getInst(botnumber)
		bot.receiveChip(chip)
		return 
				
	match = re.match(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)',line)
	if match :
		low_class, high_class = [eval(cls.capitalize()) for cls in match.groups()[1::2]]
		giver_num, low_num, high_num = [int(number) for number in match.groups()[0::2]]
		giver = Bot.getInst(giver_num)
		giver.setLowHigh(low_class.getInst(low_num),high_class.getInst(high_num))
		return


testdata = open('./10test.txt')
for line in testdata:
	parseLine(line)
print NumberedThing.INST_MAP
print Bot.COMP_TRAIL[(2,5)]


NumberedThing.INST_MAP={}
Bot.COMP_TRAIL={}


data = open('./10input.txt')
for line in data:
	parseLine(line)
	
print NumberedThing.INST_MAP
print Bot.COMP_TRAIL[(17,61)]
