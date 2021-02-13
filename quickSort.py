"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    return qs(array,l=0,r=len(array)-1)

def qs(arr,l,r):
    if l == r:
        return
    
    p = partition(arr,l,r)
   
    if p == l:
        qs(arr,p+1, r)
    elif p == r:
        qs(arr, l, p-1)
    else:
        qs(arr, l, p-1)
        qs(arr, p+1, r)
        return arr

def partition(arr,l,r):
    pivot = arr[r]
    
    i = l-1
    
    for j in range(l,r):
        
        if(arr[j]<pivot):   #bring lesser values to left side by swap arr[i+1] with arr[j]
            temp = arr[i+1]
            arr[i+1] = arr[j]
            arr[j] = temp
            
            i += 1
        
    #swap i+1 with pivot
    arr[r] = arr[i+1]
    arr[i+1] = pivot
    return i+1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
