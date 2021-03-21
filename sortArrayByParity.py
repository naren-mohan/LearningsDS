class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        lp = 0
        rp = 0
        
        while rp < len(A):
            if A[rp] % 2 == 0:
                #move left
                temp = A[lp]
                A[lp] = A[rp]
                A[rp] = temp
                
                lp += 1
            
            rp += 1
        
        return A
