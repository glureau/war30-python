#!/usr/bin/python
import copy
import wolfram30

count = int(input("Taille du triangle : "))

bufferInput = [False] * (2 * count + 1)
bufferInput[count] = True
bufferOutput = [False] * (2 * count + 1)

wolfram30.printBoolArray(bufferInput)
for line in xrange (0, count):
	for index in xrange(0, len(bufferInput)):
		bufferOutput[index] = wolfram30.computeNext(bufferInput, index)		
	wolfram30.printBoolArray(bufferOutput)
	# We could avoid this copy by swapping input/output in the compute line, but this implementation should remain very simple.
	bufferInput = copy.copy(bufferOutput)
