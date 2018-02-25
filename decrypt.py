#!/usr/bin/python
# encoding: utf-8
import copy
import libWolfram30
import libBinary

msg = raw_input("Message a decrypter : ")
code = raw_input("Clé d'encryption : ")

binaryMsg = msg
binaryCode = libBinary.textToBits(code) # 10010101
print "Message:", binaryMsg

inputLength = len(binaryCode)

bufferInput = libWolfram30.toBoolArray(binaryCode)
bufferOutput = [False] * inputLength

#libWolfram30.printBoolArray(bufferInput)

binaryMsgLength = len(binaryMsg)
xorKey = [False] * binaryMsgLength

xorKeyIndex = 0
for line in xrange (0, binaryMsgLength):
	for index in xrange(0, len(bufferInput)):
		bufferOutput[index] = libWolfram30.computeNext(bufferInput, index)
		if (index == (binaryMsgLength / 2)):
			xorKey[xorKeyIndex] = bufferOutput[index]
	xorKeyIndex += 1
	#libWolfram30.printBoolArray(bufferOutput)
	# We could avoid this copy by swapping input/output in the compute line, but this implementation should remain very simple.
	bufferInput = copy.copy(bufferOutput)



binaryMsgBA=libWolfram30.toBoolArray(binaryMsg)

xorResult = [False] * binaryMsgLength
for i in range(0, binaryMsgLength):
	xorResult[i] = (binaryMsgBA[i] != xorKey[i])

print "Xor key:",
libWolfram30.printBoolArray(xorKey)
print "Message:",
libWolfram30.printBoolArray(binaryMsgBA)
print "Result :",
libWolfram30.printBoolArray(xorResult)

xorResultStr=libWolfram30.toBinaryString(xorResult)
print "0/1 :", xorResultStr
print "Ascii (do not copy):", libBinary.bitsToTextNoEncode(xorResultStr)

