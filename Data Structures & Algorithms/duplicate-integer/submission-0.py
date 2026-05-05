class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            try:
                hash[i]+=1
            except:
                hash[i]=1
        for i in hash:
            if hash[i]>1:
                return True
        return False