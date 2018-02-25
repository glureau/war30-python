# encoding: utf-8
import sys

def printBoolArray(boolArray): 
	for x in boolArray:
		if (x):
			sys.stdout.write('█')
		else:
			sys.stdout.write(' ')
	print

def writeInP2File(file, boolArray): 
	for x in boolArray:
		if (x):
			file.write('1 ',)
		else:
			file.write('0 ',)
	file.write('\n')

def pickLeftInCyclicBuffer(array, index):
	if (index == 0):
		return array[len(array)- 1]
	else:
		return array[index-1]

def pickRightInCyclicBuffer(array, index):
	if (index == len(array) - 1):
		return array[0]
	else:
		return array[index+1]

def rule30(left, center, right):
	result=False
	if ((not left) and (not center) and right):
		result=True
	if ((not left) and center and (not right)):
		result=True
	if (left and (not center) and (not right)):
		result=True
	if ((not left) and center and right):
		result=True
	return result

def computeNext(array, index):
	left=pickLeftInCyclicBuffer(array, index)
	center=array[index]
	right=pickRightInCyclicBuffer(array, index)
	return rule30(left, center, right)		

def toBoolArray(src):
	dest = [False] * len(src)
	index = 0
	for c in src:
		if (c == "1"):
			dest[index] = True
		index+=1
	return dest

def toBinaryString(src):
	dest = ""
	for c in src:
		if (c):
			dest += "1"
		else:
			dest += "0"
	return dest
