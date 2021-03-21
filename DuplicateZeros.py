class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        k = 0
        length = len(arr)
        while (k < length):
            if arr[k] == 0:
                temp1 = 0
                for j in range(k+1, length):
                    temp2 = arr[j]
                    arr[j] = temp1
                    temp1 = temp2
                k += 2
            else:
                k += 1
        
        
