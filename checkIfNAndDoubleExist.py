class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:        
        for i, v in enumerate(arr):
            if (arr[i] * 2) in arr[i+1:] or (arr[i] * 2) in arr[:i]:
                return True
        return False
        
