from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first idea, brute force, loop through all the items in the list
        # have a nested for loop that runs through EACH item. setup a hashmap to count character count for each.
        # have logic that sorts each.
        # O(n^2) time + O(n) space

        # second idea, sort each word
        # if you sort each word then you see which words are the same. we'll keep track of where the sorted words are in relation to 
        # the original list. then you output the words that are the same
        # m * n log n time though


        res = defaultdict(list)
        
        for i in strs:
            freq = [0] * 26 # a - z

            # keep count of each character
            for x in i:
                freq[ord(x) - ord('a')]+=1 # ord() is an ascii function. provides the actual number
                # - ord("a") is because ord("a") is like valued at 97. its for balancing.
                # lets assume z is 122. 122 - 97 = 25 
                # so 25 is going to be added by one
            
            # lists cant be keys in python but TUPLES can
            res[tuple(freq)].append(i)

        return list(res.values())

