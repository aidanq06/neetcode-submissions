class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # start with 3 pointers
        # 1st pointer: 0, 2nd pointer: 1, 3rd pointer: 2
        """
        slow = 0 
        normal = 1
        fast = 2
        """
        # we cant start with a while loop thats (while slow + normal + fast = 0) because we essentially
        # could have multiple different outputs. we're expected to return ALL of the triplets
        
        nums.sort()
        # while true
        # original nums =  [-1,0,1,2,-1,-4]
        # sorted nums = [-4,-1,-1,0,1,2]
        # first run = -3
        # second run = 0

        appendList = list()
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # basically if the next value in the list is the same number then skip
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sums = nums[left] + nums[right] + nums[i]
                if sums > 0:
                    right-=1
                    continue
                elif sums < 0:
                    left +=1
                    continue
                elif sums == 0:
                    if [nums[left],nums[right],a] not in appendList: 
                        appendList.append([nums[left],nums[right],a])
                    left+=1

                    

        return appendList

        

        """
        tripletList = []
        left1 = 0
        left2 = 1
        right = len(nums)-1

        while True:
            sumPointers = nums[left1]+nums[left2]+nums[right]
            if sumPointers == 0:
                if [nums[left1],nums[left2],nums[right]] not in tripletList:
                    tripletList.append([nums[left1],nums[left2],nums[right]])
                left1+=1
                left2+=1
            elif sumPointers > 0:
                right-=1
            elif sumPointers < 0:
                left1+=1
                left2+=1
            
            if left2 == right:
                break
        return tripletList
        
        """

        
                


            




        