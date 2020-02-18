# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
    if arr[i] == target:
      return i
      break
  else:
    return -1   # not found
  # TO-DO: add missing code


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):


  if len(arr) == 0:
    return -1 # array empty
    
  # TO-DO: add missing if/else statements, recursive calls
  



lst = [1,2,3,4,5, 8,55,77,88,1000]


print(linear_search(lst, 6))
