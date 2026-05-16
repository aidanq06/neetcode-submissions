class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # so the brute force solution is just to run a for loop until target is reached
        # this solution is trivial
        

        # on second thought im thinking about using a binary search algorithm
        # the binary search algorithm will be similar to another question, finding a 
        # minimum in a rotated soarted array.

        # essentially what we have is an array, thats sorted but has been rotated n times
        # we'll start in the middle of the array

        # assume the array is [3,4,5,6,1,2]
        # the middle value (left+right)//2 == (0+5)//2 = 2
        # the middle value is nums[2] == 5

        # in the array [3,4,5,6,1,2]
        # we can break it down into 2 different sorted arrays with a "seperation point"
        # [3,4,5,6] and [1,2]
        # if we KNOW this seperation point, we can very easily narrow it down to a single value.
        # we need to compare it to the left and the right pointer to see if where we're rotated.
        # [6,7,8,9,10,1,2,3,4,5]
         #             ^        ^
           #           5        9
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        while l<=r:
            mid=(l+r)//2
            if nums[mid] == target: # best cases, the mid number is equal to the target
                return mid 
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            #if nums[l] < nums[mid] and nums[r] > nums[mid]:
                
            elif nums[l] > nums[mid]:
                if target>nums[mid] and target<nums[l]: # might be in this sorted half
                    l=mid+1
                else:
                    r=mid-1
            elif nums[r] < nums[mid]:
                if target<nums[mid] and target>nums[l]: # might be in this sorted half
                    r=mid-1
                else:
                    l=mid+1
            # normal list
            else:
                if nums[mid] > target:
                    r=mid-1
                if nums[mid] < target:
                    l=mid+1
                

            
        
        return -1 # exit condition returns -1 (not in the list)