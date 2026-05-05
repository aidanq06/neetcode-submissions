class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # brute force, duplicate list then run through second list then append to nums
        
        length = len(nums)
        for i in range(length):
            nums.append(nums[i])

        return nums