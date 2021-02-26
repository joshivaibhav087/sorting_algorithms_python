#defining function for insertion sort
def insertion_sort(arr):

    # iterate from 1 to length of array
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        # move elements thar are greater than key to one
        #position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr

# passing array
s = input("enter the sequence: ")
arr = s.split()

# calling function
print(insertion_sort(arr))
