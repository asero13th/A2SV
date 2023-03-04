class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reminder = 0
        for i in range(len(digits)- 1,-1,-1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                reminder = 1
            else:
                reminder = 0
                break
        if reminder == 1:
            digits = [1] + digits
            
        return digits