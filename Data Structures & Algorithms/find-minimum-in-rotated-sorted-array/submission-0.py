class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force is just 1 iteration of a for loop
        # or just built in python function
        # min(nums)

        # first thought.
        # when i see log n i think binary search
        # we can't normally do binary search if it has been rotated. 
        # if we check the first and last character we can see if it has been rotated
        # we're essentially just finding the break point. 

        # if we find the breakpoint, (lets say it was 4 iterations)
        # we can essentially find the minimum by ADDING that to the initial value.
        # so rotated 4 times = num[4] is the minimum
        """
        [5,0,1,2,3,4]
             ^
        [10,1,2,3,4,5,6,7,8,9]
         ^        ^         ^
        left      mid      right
        [10,1,2,3,4,5,6,7,8,9]
         ^    ^   ^
        left mid right
        [6,7,8,9,10,1,2,3,4,5]
                  ^
        [1,2,3,4,5,6,7,8,9,10]
                 ^
        """

        l = 0
        r = len(nums)-1

        # if the list is only 1 number, thats the smallest number
        while l<=r:
            mid = (l+r)//2
            if nums[l] > nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid+1
            else:
                return nums[l]
        return nums[mid]
            
        
