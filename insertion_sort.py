def insertion_sort(array):
	if len(array) < 2: return array
	key = 1

	while key < len(array):
		left = key-1
		# guard for beginning of array, left values should always be less than
		while left >= 0 and array[key] < array[left]:
			array[key], array[left] = array[left], array[key]
			# get back the key
			key = left
			left -= 1
		key += 1	
	return array	

print(insertion_sort([1, 1, 5, -6]))
print(insertion_sort([5, 3, 6, -1]))
print(insertion_sort([8, 9, -70, 9, 3]))
