# when values aren't integers
def bucket_sort(array):
  max_value = int(max(array))
  
  buckets = [[] for i in range(max_value+1)]
  for val in array:
    buckets[int(val)].append(val)
  
  i = 0
  for bucket in buckets:
    if bucket:
      array[i:i+len(bucket)] = sorted(bucket)
      i = i+len(bucket)
    
test = [4.5, 4, 7.3333, 8, 8, 1, 1.6]    
bucket_sort(test)
# [1, 1.6, 4, 4.5, 7.3333, 8, 8] 
print(test)
