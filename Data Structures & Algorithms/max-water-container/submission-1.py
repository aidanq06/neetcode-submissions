class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxHeight = 0 
        maxValue = max(heights)

        while left < right:
            # the first check
            area = min(heights[left], heights[right]) * (right-left)
            maxHeight = max(maxHeight, area)

            if heights[left] < heights[right]:
                left +=1
            elif heights[left] > heights[right]:
                right -=1
            else: # equal
                right -= 1 # either is fine
            # we're not trying to "predict" the next value. thats not classic two pointer
            """
            if (heights[left+1] * (right-left)) > sums:
                left+=1
                continue
            if (heights[right-1] * (right-left)) > sums:
                right-=1
                continue
            """



        return maxHeight

            
