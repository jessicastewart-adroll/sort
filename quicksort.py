def quicksort(array):
  if len(array) < 2: return array
  
  more = []
  less = []
  same = []
  pivot = len(array)-1
  for val in array:
    if val < array[pivot]:
      less.append(val)
    elif val > array[pivot]:
      more.append(val)
    else:
      same.append(val)
      
  qmore = quicksort(more)
  qless = quicksort(less)
  return qless + same + qmore   
  
print(quicksort([3, 7, 8, 5, 2, 1, 9, 5, 4])) 
