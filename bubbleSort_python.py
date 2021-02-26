# define a function for bubble sort(ascending order)

def bubble_sort(x):
    n = len(x)
    
    # traverse through all array elements
    for i in range(n):
        
        #last i elements already in place
        for j in range(0, n-i-1):

            #traverse array fro, 0 to n-i-1 and
            #swap if element found is greater than next element
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1], x[j]
    
#call the function

s= input("enter the sequence: ")
x =s.split() 
bubble_sort(x)
print(x)


    

    
