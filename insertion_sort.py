def insertion_sort(unsorted_array):
  sorted_array = [unsorted_array[0]]
  unsorted_index = 1
  
  while unsorted_index < len(unsorted_array):
    to_add = unsorted_array[unsorted_index]
    sorted_index = 0
    while sorted_index < len(sorted_array):
      print(sorted_index)
      if sorted_array[sorted_index] < to_add:
        sorted_index += 1
      else:
        print(sorted_index, to_add)
        sorted_array.append(unsorted_array[unsorted_index])
        break
        # sorted_array = sorted_array[:sorted_index] + [unsorted_array[unsorted_index]] + sorted_array[sorted_index:]
        # sorted_index = len(sorted_array)
    unsorted_index += 1
    
insertion_sort([3, 7, 4, 9, 5, 2, 11])
