# defining function for selection sorting
def Selection_sort(arr):

    #interation for minimum value
    for  i in range(0,len(arr)):
        minimum = i


        #find the element in remaining 
        for j in range(i+1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j

        # swap the elements if above condition is satisfied
        if minimum != i:
            arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

            
# declaring array    
arr = [5,2,7,4,8,1,9]

# calling finction
print(Selection_sort(arr))






                       
                       
                       

    
