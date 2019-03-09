#!/usr/bin/env python3

import dataset as ds
import binning
import stairify
import alignment as al
from parameter import *
import time
import threading
import queue

def getbinning(id, data, zero, reverse):
	if reverse:
		return id, binning.transform(data[::-1], zero)
	else:
		return id, binning.transform(data, zero)

def getstairs(data, wsize):
	id = data[0]
	return id, stairify.transform(len(data[1]), wsize, data[1])

class Process(threading.Thread):
	def __init__(self, r, wsize, epsilon, reverse):
		threading.Thread.__init__(self)

		rid, rdata = r[0].split()
		cid, cdata = r[1].split()

		self.rid, self.rseq = getstairs(getbinning(rid, rdata, p.zero, True), wsize)
		self.cid, self.cseq = getstairs(getbinning(cid, cdata, p.zero, reverse), wsize)

		self.epsilon = epsilon

		self.lock = threading.Lock()

		self.start()

	def printrecord(self, data):
		self.lock.acquire()
		print(data)
		self.lock.release()


	def maptostring(self, m):
		return ' '.join(['{}:{}'.format(a,b) for a,b in sorted(m.items())])

	def run(self):
		start = time.time()
		numbers, rgaps, cgaps, cstart, rstart = al.Realwater(epsilon = self.epsilon).align(self.rseq, self.cseq)
		elapsed = time.time() - start

		rgaps, cgaps = self.maptostring(rgaps), self.maptostring(cgaps)

		self.printrecord('{}\t{}\t{:0.2f}\t{:0.2f}\t{:0.1f}\t{}\t{}\t[{}]\t[{}]\t{:2.0f}'.format(self.rid,self.cid,numbers[0], numbers[1], self.epsilon, cstart, rstart, rgaps, cgaps, elapsed))

for r in ds.records(rs=2):
	for epsilon in p.epsilon.split(','):
		Process(r, int(p.windowsize), float(epsilon), int(p.reverse))
