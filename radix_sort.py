def split_into_buckets(array, digit):
	div = 1*digit
	mod = 10*digit
	buckets = [[] for i in range(10)]
	for val in array:
		d = int(val%mod/div)
		buckets[d].append(val)
	return buckets	

def merge_buckets(buckets, array):
	i = 0
	for bucket in buckets:
		for b in bucket:
			array[i] = b	
			i += 1

def radix_sort(array):
	max_val = max(array)
	passes = len(str(max_val))

	for p in range(passes):
		digit = 10**p
		buckets = split_into_buckets(array, digit)
		merge_buckets(buckets, array)

test = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(test)
print(test)	
