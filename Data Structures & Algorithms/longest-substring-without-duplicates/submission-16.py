class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0
            
        s = list(s)
        left = 0
        seenset = set()
        maxValue = 1

        for right in range(len(s)):
            if s[right] not in seenset:
                seenset.add(s[right])
            else:
                while s[right] in seenset:
                    seenset.remove(s[left])
                    left+=1
                seenset.add(s[right])
                
            maxValue = max(maxValue, len(seenset))
        return maxValue












        """
        if s == "":
            return 0
            
        s = list(s)

        left = 0
        length = 1

        seenset = set()
        
        for right in range(len(s)):
            if s[right] not in seenset:
                seenset.add(s[right])
            else:
                left+=1
                seenset = set()
                for i in range(left,right+1):
                    seenset.add(i)
            length = max(length, len(seenset)) 
        
        return(length)
        """

            
            