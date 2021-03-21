class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        increasing = True
        mountain = False
        
        for i, v in enumerate(arr):
            if i == 0:
                continue
            
            if increasing and arr[i] <= arr[i-1]:
                if i == 1:
                    return False
                increasing = False
                
            if not increasing:
                print("hi")
                if arr[i] >= arr[i-1]:
                    return False
                else:
                    mountain = True
        
        if not mountain:
            return False
        else:
            return True
                
            
