class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # original two sum is O(n) time and O(n) space (hashmap)
        # already sorted

        # pointer will hold the indexes
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

        
            