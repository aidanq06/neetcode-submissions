class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        final, current = [], []
        nums = list(range(1,n+1))

        def backtrack(i, current):
            if i >= len(nums):
                if len(current) == k:
                    final.append(current.copy())
                return

            current.append(nums[i])
            backtrack(i+1,current)

            current.pop()
            backtrack(i+1,current)

        backtrack(0,current)
        return final