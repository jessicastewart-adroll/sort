def partition(array):
  if len(array) < 2: return array
  
  pivot = len(array)-1
  i = pivot-1
  while i >= 0:
    if array[i] > array[pivot]:
      array[i], array[pivot] = array[pivot], array[i]
      pivot = i
    i -= 1
    
  return partition(array[:pivot]) + partition(array[pivot:])
  
def quicksort(array):
  return partition(array)
  
print(quicksort([3, 4, 5, -9, 0, -7]))  
