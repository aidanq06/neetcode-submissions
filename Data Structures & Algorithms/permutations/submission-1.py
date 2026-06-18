class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # lets assume our example is [1,2,3]
        # we first start at index 0, so 1
        # for 1, we have to create permutations with 2 and 3
        # for 2, we can do 1,2 and 2,1
        # then for 3 we can do 1,2,3, 1,3,2, 3,1,2 and 3,2,1, 2,3,1 and 2,1,3
        # what we're doing here is we're inserting inbetween each number in each of the "permutations"
        # then we are also inserting at the start and the end

        def backtrack(i):
            if i >= len(nums):
                return [[]]

            current = []
            
            
            permutation = backtrack(i+1)

            # lets assume its base case right now, [[]]
            for p in permutation:
                # for [] in []
                for insertion in range(len(p)+1): # we have to insert at every position, therefore
                # we need to do +1. 
                    pCopy = p.copy()
                    pCopy.insert(insertion, nums[i])
                    current.append(pCopy)

            # [[]]
            # [[3]] second iteration?
            # [[2,3],[3,2]] third iteration
            # [[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]]    
            
            return current

        return backtrack(0)
