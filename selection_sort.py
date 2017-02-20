def selection_sort(array):
  if len(array) < 2: return array
  
  i = 0
  while i < len(array)-1:
    min_index = i
    j = i + 1
    while j < len(array):
      if array[min_index] > array[j]:
        min_index = j
      j += 1   
    array[i], array[min_index] = array[min_index], array[i]
    i += 1 
  print(array)  
  return array  

selection_sort([3, -9, -5, 100, -5, 3])
