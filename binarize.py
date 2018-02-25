#!/usr/bin/python
# encoding: utf-8
import libBinary

msg = raw_input("Message a binariser : ")
print libBinary.textToBits(msg)


#import sys

#msg = raw_input("Message a binariser : ")

#for c in msg:
#	print(c + " = " + str(bin(ord(c)))[2:].zfill(8))

#print "message with spaces:",
#for c in msg:
#	print str(bin(ord(c)))[2:].zfill(8),
#print

#print "message: ",
#for c in msg:
#	sys.stdout.write(str(bin(ord(c)))[2:].zfill(8))
#print
