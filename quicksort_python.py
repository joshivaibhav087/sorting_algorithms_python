# function to quick sort algorithm
def quick_sort(arr):
    n = len(arr)

    # if one element is present in array return the array
    if n <= 1:
        return arr
    else:
        pivot = arr.pop()   # taking last element of array as pivot

    quick_greater = []
    quick_smaller = []

    # iterating over  an array 
    for i in arr:
        if i > pivot:
            quick_greater.append(i)

        else:
            quick_smaller.append(i)
            
    return quick_sort(quick_smaller) + [pivot] + quick_sort(quick_greater)

# defining array
arr = [5,1,6,2,7,3,8]

# calling function 
print(quick_sort(arr))

    


