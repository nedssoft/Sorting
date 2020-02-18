# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    
     # Initialize an empty array
    merged_arr = []
    
    # Loop through the two arrays, compare elements
    # pop the smallest element and append to the merged_arr
    while len(arrA) and len(arrB):

        if (arrB[0] > arrA[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    
    # Once one of the array is exhausted, check if the other is yet to be exhausted

    # Check if arrA has some elements left
    if len(arrA):
        #  Sort the elements
        for i in range(len(arrA) - 1):
            if arrA[i] > arrA[i+1]:
                arrA[i], arrA[i+1] = arrA[i+1], arrA[i]
    # Add the elements to the merged_arr
    merged_arr += arrA

    # Check if arrB has some elements left
    if len(arrB):
        for i in range(len(arrB) - 1):
            if arrB[i] > arrB[i+1]:
                arrB[i], arrB[i+1] = arrB[i+1], arrB[i]
    
    # Add the elements to the merged_arr
    merged_arr += arrB

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort(arr):

    if (len(arr) <=1 ):
        return arr
    # Get the middle of the array
    mid = len(arr) // 2
    # Get the LHS
    left = arr[:mid]
    #Get the RHS
    right = arr[mid:]

    # Repeat the process above for each part until it reaches base case
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the two arrays
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


print(merge([1,2,3], [2,47,4,5]))

print(merge_sort([1,2,3,2,47,4,5]))
