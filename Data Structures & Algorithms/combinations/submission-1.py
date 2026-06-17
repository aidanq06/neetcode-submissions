class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        final, current = [], []
        nums = list(range(1,n+1))
        # assume n = 3
        # [1,2,3]
        # 

        def backtrack(i, current):
            # if i is greater than the length of the entire. number, then we can't continue
            if len(current) == k:
                final.append(current.copy())
                return
            
            if i >= len(nums):
                return

            

            current.append(nums[i])
            backtrack(i+1,current)

            current.pop()
            backtrack(i+1,current)

        backtrack(0,current)
        return final