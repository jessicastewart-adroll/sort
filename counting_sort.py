def counting_sort(array):
	max_value = array[0]
	for i in array[1:]:
		max_value = max(max_value, i)

	counts = [0 for i in range(max_value+1)]	
	for i in array:
		counts[i] += 1	

	j = 0
	for i, x in enumerate(counts):
		while x > 0:
			array[j] = i
			j+=1
			x-=1						

test = [1, 4, 1, 2, 7, 5, 2]
print(test)
counting_sort(test)	
print(test)	
# [1, 1, 2, 2, 4, 5, 7]
