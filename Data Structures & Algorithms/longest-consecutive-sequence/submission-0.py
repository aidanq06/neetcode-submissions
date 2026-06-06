class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the brute force solution is to sort the array
        # then run a for loop to see if each value AFTER the current is exactly adding +1 if it isnt they 
        # output the counter

        # check the list at most 2 times
        nums = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in nums:
                length = 0
                while (i + length) in nums:
                    length+=1
                longest = max(length, longest)
        
        return longest