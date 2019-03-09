import textwrap as tw

ZERO = '0'
ONE = '1'

def replace(s, zero):
	return ''.join([ZERO if a in zero else ONE for a in s])

def pack(data, zero):
	lst = tw.wrap(data,4)

	lst = ['{:<04}'.format(replace(s,zero)) for s in lst]

	return ''.join(['{:X}'.format(int(a,2)) for a in lst])


def atransform(id, datasize, data, zero, sink):
	sink.head(id, datasize)
	sink.tail(pack(data.upper(),zero))
	sink.end()

def transform(data, zero):
	return pack(data.upper(),zero)

