class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length1 = len(nums)
        temp = []
        while(k < length1):
            #print(nums[k])
            if nums[k] != val:
                temp.append(nums[k])     
            k += 1
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        nums = nums[:len(temp)]
        return len(nums)
