class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the brute force solution is to run something like a nested for loop, where for each value,
        # we essentially just "pop" the current value out then multiply each item in the list and add it to a
        # final list.
        # this solution would be an O(n^2) time solution however, since for each value in the list, we're comparing it 
        # against all the other values in the list again.
        
        # we should essentially be able to ONLY have to iterate through the list one time to get all the values
        # additionally, the lists should match up.
        # so nums[i] should correlate to output[i], the order matters, 
        # what we can do is do something called a prefix and a postfix solution
        # essentially if we're at an array like [1,2,3,4]
        # and we need to calulate the product excluding 3.
        # we can do 1 * 2 and 4.
        # we can have a prefix array which is [1,2,6,24]
        # then a postfix array which is [4,12,24,24]
        # the product without 3 is 8. so 2 * 4.
        final = []
        prefix = [1]
        curr = 1
        for i in range(len(nums)):
            curr*=nums[i]
            prefix.append(curr)

        postfix = []
        curr = 1
        for i in range(len(nums)-1,-1,-1):
            curr*=nums[i]
            postfix.append(curr)

        postfix = postfix[::-1]
        postfix.append(1)
        
        for i in range(len(nums)):
            final.append(prefix[i]*postfix[i+1])
        
        return final
        
        
        # 1, 2, 4, 6
        # (1) * (4*6)
      
        # 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8
        #. 1 , 2 , 6 , 24 ^  336 ,  56 , 8
        # prefix[i] should be the product of everything before i
        # postfix[i] should be the product of everything after i