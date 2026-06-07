class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        # O(n) solution
        
        final = []
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
        
        sortedMap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        
        counter = 0
        while counter != k:
            key = list(sortedMap.keys())[counter]
            final.append(key)
            counter+=1
        return(final)
        
        
        