class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #finding max 1s 
        
        max_res = 0
        temp = 0
        
        for num in nums:
            
            if num == 1:
                temp += 1
            else:
                temp = 0
                        
            if temp > max_res:
                max_res = temp
                
        return max_res
