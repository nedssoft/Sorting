# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(smallest_index +1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
            
        # TO-DO: swap
        arr[cur_index], arr[smallest_index]  = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    max_index = len(arr) - 1;
    for i in range(max_index):
        for j in range(max_index):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

print(selection_sort([2,31,6]))
print(bubble_sort([2,31,6]))