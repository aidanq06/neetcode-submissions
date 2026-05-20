class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force is a seen approach
        # however this approach isn't space efficient

        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return i

        