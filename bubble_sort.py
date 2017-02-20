def bubble_sort(array):
  if len(array) < 2: return array

  i = 0
  
  while i < len(array):
    j = 0
    swap = False
    while j < len(array)-1:
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
        swap = True
      j += 1  
    if swap == False: return array  
    i += 1  
      
print(bubble_sort([6, -4, 7, 8, -90, -4]))
