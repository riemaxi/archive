import sys
import itertools as it

OK = lambda r : True
END = lambda r : False

RECORD_SIZE = 1

def records(input = sys.stdin, rs = RECORD_SIZE, ok = OK, end = END):

	def nextrecord(input, rs):
		try:
			return [x.strip() for x in it.islice(input,rs)]
		except:
			return None

	r = nextrecord(input, rs)
	while r:
		if ok(r):
			yield r

		if end(r):
			break

		r = nextrecord(input, rs)

def pairs(inputa = sys.stdin,inputb=sys.stdin, rs=1):
	for a,b in  it.product(records(inputa,rs), records(inputb,rs)):
		yield a,b
