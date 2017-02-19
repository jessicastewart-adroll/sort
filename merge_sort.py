def merge(left, right):
  left_index = 0
  right_index = 0
  result = []
  
  while left_index < len(left) and right_index < len(right):
    if left[left_index] <= right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1
    
  # if len(left)-1 > left_index:
  #   result.extend(left[left_index+1:])
  # if len(right)-1 > right_index:
  #   result.extend(right[right_index+1:])  
  print(result)
  return result  
  
def merge_sort(array):
  if len(array) == 1:
    return array
    
  mid = len(array)//2  
  left = array[:mid]
  right = array[mid:]
  left = merge_sort(left)
  right = merge_sort(right)
  
  return merge(left, right)

test_one = [5, 12, -3, 900]
merge_sort(test_one)  
