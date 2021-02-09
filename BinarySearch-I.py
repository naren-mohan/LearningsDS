"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    length = len(input_array)
    start_index = 0
    end_index = length-1
    
    while(1):
        mid_index = float(((end_index - start_index + 1) / 2.0) + start_index)
        
        mid = input_array[int(mid_index)]
        if(mid == value):
            return int(mid_index)
        elif(start_index == end_index):
            break
        elif(value > mid):
            start_index = int(mid_index + 1)
        else:
            end_index = int(mid_index - 1)
        
            
        
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
