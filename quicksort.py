def partition(array):
  if len(array) < 2: return array
  
  pivot = len(array)-1
  i = pivot-1
  while i >= 0:
    while array[i] > array[pivot]:
      array[i], array[i+1] = array[i+1], array[i]
      pivot = i
      i = pivot-1
    i -= 1  
  print(array)  
  #return partition(array[:pivot]) + [pivot] + partition(array[pivot+1:])
  
def quicksort(array):
  partition(array)
  
print(quicksort([3, 7, 8, 5, 2, 1, 9, 5, 4]))  
