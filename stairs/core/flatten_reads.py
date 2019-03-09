#!/usr/bin/env python3

import math
import dataset as ds
from constant import *

RECORD_SIZE = 4

def code(b, q):
	q = min(ord(q)-PHRED_START,PHRED_SIZE-1)

	return chr(PHRED_START + PHRED_SIZE*LETTER.index(b) + q)


def compress(seq, qual):
	return ''.join([code(seq[i], qual[i]) for i in range(len(qual))])

for r in ds.records(rs=RECORD_SIZE):
	try:
		print(r[0].split()[0], compress(r[1], r[3]), sep='\t')
	except:
		break
