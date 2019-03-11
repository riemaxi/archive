#!/usr/bin/env python3

import dataset as ds
from parameter import *

minsize = int(p.reads_minsize)
maxnumber = int(p.reads_maxnumber)

for r in ds.records(end = lambda r : not maxnumber):
	id, data = r[0].split('\t',2)

	if len(data) >= minsize:
		print(r[0])

		maxnumber -= 1
