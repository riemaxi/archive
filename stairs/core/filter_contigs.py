#!/usr/bin/env python3

import dataset as ds
from parameter import *

minsize = int(p.contigs_minsize)
for r in ds.records(ok = lambda r: len(r[0].split()[1]) >= minsize):
	print(r[0])
