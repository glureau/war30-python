#!/usr/bin/python
import copy
import wolfram30

count = int(input("Taille du triangle : "))

bufferInput = [False] * (2 * count + 1)
bufferInput[count] = True
bufferOutput = [False] * (2 * count + 1)

file = open("output.pgm", "w")

file.write("P1\n")
file.write(str(2 * count + 1) + ' ' + str(count) + '\n')
 
wolfram30.writeInP2File(file, bufferInput)
for line in xrange (0, count):
	for index in xrange(0, len(bufferInput)):
		bufferOutput[index] = wolfram30.computeNext(bufferInput, index)		
	wolfram30.writeInP2File(file, bufferOutput)
	# We could avoid this copy by swapping input/output in the compute line, but this implementation should remain very simple.
	bufferInput = copy.copy(bufferOutput)
file.close() 
