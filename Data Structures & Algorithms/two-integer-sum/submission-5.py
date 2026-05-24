class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # two pointer only works for sorted arrays
        """
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            sums = nums[left]+nums[right]
            if sums > target:
                right-=1
            elif sums < target:
                left+=1
            else:
                return [left,right]
        """
        hashmap = {}
        for i,a in enumerate(nums):
            if target - a in hashmap:
                return [hashmap[target-a],i]
            else:
                hashmap[a] = i
            

