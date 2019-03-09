#!/usr/bin/env python3

import dataset as ds
from parameter import *
import sys

for c,r in ds.pairs(inputb = open(sys.argv[1])):
	rid, rdata = c[0].split()
	cid, cdata = r[0].split()

	print(c[0])
	print(r[0])
