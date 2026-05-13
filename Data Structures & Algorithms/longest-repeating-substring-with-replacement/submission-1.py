class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        s = list(s)
        left = 0    
        maxLength = 0
        frequency = {}
        for right in range(len(s)):
            # if the value IS in frequency then we want to update it else just create new
            if s[right] not in frequency:
                frequency[s[right]]=1
            else:
                frequency[s[right]]+=1
            
            longestFrequency = max(frequency.values())
            length = (right-left+1)
            while (length - longestFrequency) > k: #if the length of the substring
            # MINUS the number of characters with longest frequency is LESS than the
            # replaceable amount, we have to move the left pointer to satisfy the k again.
                print(frequency)
                frequency[s[left]]-=1
                left+=1
                length = (right-left+1) 
                
            maxLength = max(maxLength, right-left+1)
        
        return maxLength



            


        """
        # edge case: if the length is 1, longest substring is going to be 1
        if len(s) == 1:
            return 1

        s = list(s)

        # we can't add 2 if the total output is going to be greater than the length
        # we need to evaluate if the right value is equal to the previous value first
        # because, if we update the length without evaluating first it can add 1
        left = 0
        length = 0

        for right in range(1,len(s)):
            if s[right] != s[left] and s[min(right+1,len(s)-1)] != s[left]:
                left=right
            length = max(length, right-left+1+k)
        return length
        """
            