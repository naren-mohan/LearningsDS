class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        moves = 0
        tempheights = [None] * len(heights)
        for i in range(len(heights)):
            tempheights[i] = heights[i]
            
        heights.sort()
        
        # print(heights)
        # print(tempheights)

        for i in range(len(heights)):
            if heights[i] != tempheights[i]:
                moves += 1        
        
        return moves
