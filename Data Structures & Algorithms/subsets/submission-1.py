class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # basically we want to think of this problem like a decision tree.

        # at each number we want to create a list that HAS the value and DOESNT have the value.
        # e.g. lets assume nums = [1,2,3]

                                # [1]
                            #[1]        #[]
                        #[1,2]   [1]   #[2]    #[0]
            # [1,2,3] [1,2]    [1,3]  [1]  [2,3] [2]  [3] [0]
        
        # this shows every possible combination of numbers in a list. 
        # permutation is different, permutation is specific about the positioning of the numbers

        # for example [1,2,3] and [3,2,1] are equivalent in combination
        # but they are different in permutation


        final, current = [],[]
        

        def backtrack(i, current):
            # basically when we reach the END of the list, we want to copy the current list. WE CANT directly append the current list without copying because lists are mutable and if you change something with current it could directly change IN the final list
            if i>=len(nums):
                final.append(current.copy())
                return
            
            # this is the left decision, essentially we want to ADD the current value
            current.append(nums[i])
            backtrack(i+1, current)


            # this is the RIGHT decision, essentially we want to REMOVE the current value but still backtrack.
            current.pop()
            backtrack(i+1,current)

        
        backtrack(0, current)
        return final
