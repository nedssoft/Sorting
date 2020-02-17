# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    
    merged_arr = []

    while len(arrA)  and  len(arrB):
       if (arrB[0] > arrA[0]):
           merged_arr.append(arrA.pop(0))
       else:
            merged_arr.append(arrB.pop(0))
    # TO-DO
    
    if (len(arrA)):
        for i in range(len(arrA) -1 ):
            if arrA[i] > arrA[i+1]:
                arrA[i], arrA[i+1] = arrA[i+1], arrA[i]
    merged_arr += arrA

    if (len(arrB)):
        for i in range(len(arrB) -1 ):
            if arrB[i] > arrB[i+1]:
                arrB[i], arrB[i+1] = arrB[i+1], arrB[i]
    merged_arr += arrB
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    
    mid_index = len(arr)//2
    left = merge_sort(arr[:mid_index])
    right = merge_sort(arr[mid_index:])

    arr = merge(left, right)
    return arr


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
