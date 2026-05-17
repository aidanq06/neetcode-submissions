class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits[::-1]
        digits[0]+=1
        for i in range(len(digits)):
            if (digits[i] > 9) and (i+1 > len(digits)-1): #if number is greater than 10 and theres nno number after
                digits.append(1)
                digits[i] = 0
            elif digits[i] > 9:
                digits[i] = 0
                digits[i+1]+=1
            elif digits[i]+1 < 9:
                break
            
            # 9 9 9 8
            # 0 0 0 
            
            
        return digits[::-1]