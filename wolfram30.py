#!/usr/bin/python
import copy
import sys

bufferInput = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
bufferOutput = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

def foo(bar): 
	for x in bar:
		if (x):
			sys.stdout.write('#')
		else:
			sys.stdout.write(' ')
	print

foo(bufferInput)
for line in xrange (0, 500):
	for index in xrange(0, len(bufferInput)):

		if (index == 0):
			left=bufferInput[len(bufferInput)- 1]
		else:
			left=bufferInput[index-1]

		center=bufferInput[index]

		if (index == len(bufferInput) - 1):
			right=bufferInput[0]
		else:
			right=bufferInput[index+1]


		result=False
		if ((not left) and (not center) and right):
			result=True
		if ((not left) and center and (not right)):
			result=True
		if (left and (not center) and (not right)):
			result=True
		if ((not left) and center and right):
			result=True
		#print "left:", left, "  center:", center, "  right:", right, "    => ", result
		bufferOutput[index] = result		
	foo(bufferOutput)
	bufferInput = copy.copy(bufferOutput)

