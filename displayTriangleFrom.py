#!/usr/bin/python
# encoding: utf-8
import copy
import libWolfram30

baseTriangle = raw_input("Base du triangle : ")
count = int(input("Nombre d'itérations : "))

inputLength = len(baseTriangle)

bufferInput = [False] * (2 * count + inputLength)
index = count
for c in baseTriangle:
	if (c=="1"):
		bufferInput[index] = True
	index+=1
bufferOutput = [False] * (2 * count + inputLength)

libWolfram30.printBoolArray(bufferInput)
for line in xrange (0, count):
	for index in xrange(0, len(bufferInput)):
		bufferOutput[index] = libWolfram30.computeNext(bufferInput, index)		
	libWolfram30.printBoolArray(bufferOutput)
	# We could avoid this copy by swapping input/output in the compute line, but this implementation should remain very simple.
	bufferInput = copy.copy(bufferOutput)
