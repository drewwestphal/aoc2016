#!/usr/bin/python

class walker:

    rose = ['n','e','s','w']

    def __init__(self):
        self.roseptr = 0
        self.e_w_axis = 0
        self.n_s_axis = 0
        self.places_been = []


    def turnLeft(self):
        self.roseptr = 3 if self.roseptr==0 else self.roseptr-1

    def turnRight(self):
        self.roseptr = (self.roseptr+1)%4

    def curDir(self):
        return walker.rose[self.roseptr]

    def goNPaces(self, n):
    	for i in range(n):
            if self.curDir()=='n':
                self.n_s_axis+=1
            if self.curDir()=='s':
                self.n_s_axis-=1
            if self.curDir()=='e':
                self.e_w_axis+=1
            if self.curDir()=='w':
                self.e_w_axis-=1
            self.recordPosition()

    def doStep(self, step):
        if step[:1]=='L':
            self.turnLeft()
        else:
            self.turnRight()

        self.goNPaces(int(step[1:]))
        
    def recordPosition(self):
    	self.places_been.append((self.e_w_axis, self.n_s_axis))

    def printPosition(self):
        print (self.e_w_axis,self.n_s_axis)
        
    def bunnyCoords(self):
        for idx,tuple in enumerate(self.places_been):
            if self.places_been[:idx+1].count(tuple) == 2:
                print(tuple)
                return

    		

directions = ['L2','L5','L5','R5','L2','L4','R1','R1','L4','R2','R1','L1','L4','R1','L4','L4','R5','R3','R1','L1','R1','L5','L1','R5','L4','R2','L5','L3','L3','R3','L3','R4','R4','L2','L5','R1','R2','L2','L1','R3','R4','L193','R3','L5','R45','L1','R4','R79','L5','L5','R5','R1','L4','R3','R3','L4','R185','L5','L3','L1','R5','L2','R1','R3','R2','L3','L4','L2','R2','L3','L2','L2','L3','L5','R3','R4','L5','R1','R2','L2','R4','R3','L4','L3','L1','R3','R2','R1','R1','L3','R4','L5','R2','R1','R3','L3','L2','L2','R2','R1','R2','R3','L3','L3','R4','L4','R4','R4','R4','L3','L1','L2','R5','R2','R2','R2','L4','L3','L4','R4','L5','L4','R2','L4','L4','R4','R1','R5','L2','L4','L5','L3','L2','L4','L4','R3','L3','L4','R1','L2','R3','L2','R1','R2','R5','L4','L2','L1','L3','R2','R3','L2','L1','L5','L2','L1','R4']

walker = walker()

for step in directions:
    walker.doStep(step)

walker.printPosition()
walker.bunnyCoords()