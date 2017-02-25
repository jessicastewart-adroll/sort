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

### in-place ###
def partition(array, start, end):
  pivot = end
  i = pivot-1
  while i >= start:
    j = i
    while j < pivot and j >= i:
      if array[pivot] < array[j]:
        # swap
        pivot, j = j, pivot
      j -= 1  
    i -= 1
  return pivot
    
  
def quicksort(array, start=0, end=None):
  if not end:
    end = len(array)-1
  if end <= 0: return  

  pivot = partition(array, start, end)
  print(start, end, array, pivot)
  # first half
  quicksort(array, start, pivot-1)
  # second half
  quicksort(array, pivot+1, end)
  
quicksort([3, 2, 1])  
