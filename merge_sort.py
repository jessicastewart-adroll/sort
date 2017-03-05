def divide(array, start, end):
  if end == start:
    print(array[start])
    return
  
  mid = end//2 + start
  divide(array, start, mid)
  divide(array, mid, end)

def merge_sort(array):
  divide(array, 0, len(array)-1)
    
  
merge_sort([-1, -2, -3, -4, -5]) 
