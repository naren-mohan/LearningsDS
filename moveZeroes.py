class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lp = 0 
        rp = 0
        
        while rp < len(nums):
            if nums[rp] != 0:
                nums[lp] = nums[rp]
                
                if rp != lp:
                    nums[rp] = 0
                lp += 1
            rp += 1

            
                
