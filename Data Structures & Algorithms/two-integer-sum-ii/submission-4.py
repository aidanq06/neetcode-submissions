class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # original two sum is O(n) time and O(n) space (hashmap)
        # already sorted

        # we want to use the fact that its already sorted to our advantage. 
        # we'll start with the standard two pointers approach. 
        # we'll have a left and right pointer. however, we check at each iteration,
        # if that add up are greater than the target, we're going to want to reduce the right pointer
        # likewise is its less than the target, we're going to want to increase the right pointer. 
        # in the question, it states the index1 always has to be less than index2, therefore we cover that edge case
        # automatically. this solution doesn't use any additional list/datastructure and therefore its O(1) space
        """ brute force
        slow = 0
        fast = 1

        while numbers[slow] + numbers[fast] != target:
            if fast+2 > len(numbers)-1:
                fast = (fast-len(numbers)) + 2
            else:
                fast+=2
            if slow+1 > len(numbers)-1:
                slow = (slow-len(numbers)) + 1
            else:
                slow+=1

        return [slow+1,fast+1]
        """

        left = 0
        right = len(numbers)-1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right-=1
            else:
                left+=1

        return [left+1,right+1]

        
            