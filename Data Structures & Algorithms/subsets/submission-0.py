class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # basically combinations from discrete math
        # each value in the input list is unique, so we dont need to deal with values that show up multiple times
        # lets walk through the [1,2,3] example
        # when we first receive 1. We want to produce 2 new lists. 1 that includes 1 and one that doesnt. 
        # we want to 


        #              [1] []
        #      [1,2] [1] [2] [0]
        #  [1,2,3][1,2] [1,3][1] [2,3][2] [3][0]
        curr = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                curr.append(subset.copy())
                return
            
            # choice 1 include nums[i]
            subset.append(nums[i])
            backtrack(i+1)

            # undo the choice
            subset.pop()

            # choice 2 dont include nums[i]
            backtrack(i+1)

            
        backtrack(0)

        return curr