#!/usr/bin/python

import itertools

def checkTriangle(s1,s2,s3):
	for perm in itertools.permutations([s1,s2,s3]):
		if not perm[0]+perm[1]>perm[2]:
			return False
	return True

#valid = filter(checkTriangle, open('./3input.txt'))

trianglerows = [[int(x) for x in line.split()] for line in open('./3input.txt')]
validrows = filter(lambda row: checkTriangle(*row), trianglerows)

print 'valid rows: ', len(validrows)

trianglecolumn = [row[0] for row in trianglerows]+[row[1] for row in trianglerows]+[row[2] for row in trianglerows]
newrows = [trianglecolumn[i:i + 3] for i in xrange(0, len(trianglecolumn), 3)]
validcols = filter(lambda row: checkTriangle(*row), newrows)

print 'valid cols: ', len(validcols)
