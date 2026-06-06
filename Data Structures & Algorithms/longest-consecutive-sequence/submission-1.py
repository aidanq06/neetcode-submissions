class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # essentially the brute force solution/trivial solution is to
        # sort the list then wee if each additional value after that is increasing or the same.
        # if the next value is the same, keep the counter the same, but if the next value is exactly
        # +1, then add 1 to the counter.
        # this solution however is O(n log n) time since pythons sorting feature is an O(n log n) 
        # function.

        # what we can do is kind of form "GROUPS" of sequeunces. 
        # if you visualize it out, you can see that theres always a START of a sequence.
        # how do we know if something is the start of a sequence, if there is a value BEFORE it.
        # we can go through each item and check if its the start of the sequence if it has a number
        # thats before it.
        # what we can do is that if it IS a list, we can keep iterating PAST that number, checking if lets say, 
        # 3 exists in the list. then 4 exists in the list. if all of these exist in the list we'll keep adding to the lenght
        # if they dont, we can just cut the length there then take the max of it.
        # we only want to evaluate this if its at the start of the list to avoid overchecking other values. 

        # the last thing we need to realize is that
        # checking if a value is IN a list is an O(n) operation in python. therefore just normally checking if each
        # value in a list is already in the list e.g.
        # for i in list
        #      if i in list
        # is an O(n^2) algorithm
        # we need to use a set so that checking if an item is in the set is actually only an O(1) operation.
        # set membership checking is only O(1)

        nums = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in nums:
                length = 1
                while i+length in nums:
                    length+=1
                longest = max(longest,length)

        return longest