class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_index = len(arr) - 1
        right_val = arr[right_index]
        arr[right_index] = -1       #temp
        
        while(right_index > 0):
            right_index -= 1
            
            temp = max(max(arr[right_index+1:]), right_val)
            right_val = arr[right_index]
            arr[right_index] = temp
            
        return arr
