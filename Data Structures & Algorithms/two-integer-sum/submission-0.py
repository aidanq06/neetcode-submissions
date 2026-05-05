class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force solution, 2 different for loops, compare each number in the list to each other

        # ideal solution: hashmap
        hashmap = {}
        for ind, val in enumerate(nums):
            print(hashmap)
            if val not in hashmap:
                hashmap[val] = ind
            if target-val in hashmap and ind != hashmap[target-val]:
                templist = [ind, hashmap[target-val]]
                templist.sort()
                return templist
            