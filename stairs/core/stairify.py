def window(data, realsize, wsize,start,q):
	size = len(data)

	if start>=size-1:
		return None,None,None

	for i in range(start, size-1):
		q += '{:>04b}'.format(int(data[i],16))

		if len(q)>=wsize:
			return q[:wsize], q[wsize:],i+1

	if realsize % 4:
		q += '{:>04b}'.format(int(data[start-1],16))[:realsize % 4]
	else:
		q += '{:>04b}'.format(int(data[start-1],16))

	return q,'',size-1

def first_reduction(w):
	return [w.count('1'), w[int(len(w)/2):].count('1'),w,w] if w else [0,0,None,None]

def reduction(w, overlap):
	if w:
		ff = w.count('1')
		return [ff + overlap, ff, w]
	else:
		return [0,0,None]


def transform(seqsize, wsize, data):
	step = int(wsize/2)

	w, qrest, start = window(data,seqsize,wsize,0,'')
	ff, overlap, w, fw = first_reduction(w)

	vector = []
	while w:
		vector += [ff*100/wsize]

		w, rest, start = window(data,seqsize,step, start,qrest)
		ff, overlap, w = reduction(w, overlap)

	return vector
