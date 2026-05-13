class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n) time and O(1) space
        # essentially we want to do a sliding window approach
        # the window will be a fixed length of whatever length s1 is

        left = 0
        windowSize = len(s1)

        permutations = {} # measures the frequency of each character
        for i in s1:
            if i in permutations:
                permutations[i]+=1
            else:
                permutations[i]=1
        #print(permutations)
        #print(windowSize-1)
        #print(s2[windowSize-1])
        #print(range(windowSize-1,len(s2)))

        if len(s2) < len(s1): # ANY permutations of s1 cant be in s2 if its smaller. 
            # e.g. s1 = abc s2 = bc
            return False

        # sliding window
        for right in range(windowSize-1, len(s2)):
            # if each value within the window ISN'T in the permutations (has to match exactly) then it isn't valid
            windowPerms = {}
            for i in range(left,right+1):
                if s2[i] in windowPerms:
                    windowPerms[s2[i]]+=1
                else:
                    windowPerms[s2[i]]=1
            print(windowPerms)
            if windowPerms == permutations:
                return True
            else:
                left+=1
        return False    

