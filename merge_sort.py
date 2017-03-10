def merge(A, B):
  C = []
  while A and B:
    if A[0] <= B[0]:
      C.append(A[0])
      A = A[1:]
    else:
      C.append(B[0])
      B = B[1:]
      
  if A:
    C.extend(A)
  if B:
    C.extend(B)
  return C  
  
def merge_sort(input_list):
  if len(input_list) == 1:
    return input_list
  
  mid = len(input_list)//2
  left = merge_sort(input_list[:mid])
  right = merge_sort(input_list[mid:])
  return merge(left, right)
  
print(merge_sort([100, 3, -1, 4, -7]))
