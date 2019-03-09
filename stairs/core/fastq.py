#!/usr/bin/env python3
import dataset as ds
from constant import *
import sys

def phred(code):
	return chr( (ord(code) - PHRED_START)%PHRED_SIZE + PHRED_START)

def letter(code):
	return LETTER[int((ord(code) - PHRED_START)/PHRED_SIZE)]

def decompress(data):
	return ''.join([letter(code) for code in data]), ''.join([phred(code) for code in data])


def sequence(data):
	return ''.join([letter(code) for code in data])

def printall():
	for r in ds.records():
		id, data = r[0].split('\t',2)

		seq, qual = decompress(data.strip())

		print(id,seq,'+',qual, sep='\n')

def printsequence():
	for r in ds.records():
		id, data = r[0].split('\t',2)

		print(id,sequence(data.strip()),sep='\t')

if sys.argv[1] == '0':
	printall()
else:
	printsequence()
