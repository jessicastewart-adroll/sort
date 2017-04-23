### with prefix sum
def counting_sort(array):
  m = max(array)
  
  counts = [0]*(m+1)
  
  for i in array:
    counts[i] += 1
    
  i = 1
  while i < len(counts):
    counts[i] = counts[i] + counts[i-1]
    i += 1  
  
  i = 0
  while i < len(counts)-1:
    if counts[i] != counts[i+1]:
      array[counts[i]:counts[i+1]] = [i+1]*(counts[i+1]-counts[i])
    i += 1  
    
test = [4, 4, 7, 8, 8, 1]    
counting_sort(test)
print(test)
# [1, 4, 4, 7, 8, 8]

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
