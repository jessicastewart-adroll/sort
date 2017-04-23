def insertion_sort(array):
	i = 1
	n = len(array)

	while i < n:
		current = array[i]

		j = i-1
		while j >= 0 and current < array[j]:
			array[j+1] = array[j]
			j -= 1
		array[j+1] = current	
		i += 1


is_test = [12, 11, 13, 5, 6]
print('BEFORE', is_test)
insertion_sort(is_test)
print('AFTER', is_test)

def bucket_sort(array):
	buckets = [[] for i in range(10)]
	for val in array:
		index = int(val*10)
		buckets[index].append(val)

	result = []
	for bucket in buckets:
		insertion_sort(bucket)
		result.extend(bucket)

	return result

test = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print('BEFORE', test)
print('AFTER', bucket_sort(test))
