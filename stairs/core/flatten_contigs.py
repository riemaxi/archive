#!/usr/bin/env python3

import dataset as ds

print(next(ds.records())[0], end= '\t')

for r in ds.records():
	line = r[0]
	print('\n{}\t'.format(line) if line.startswith('>') else line, end = '')
print()
