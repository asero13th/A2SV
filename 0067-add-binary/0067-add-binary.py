class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = list(reversed(a))
        num2 = list(reversed(b))
        ans = []
        i,j = 0,0
        remainder = 0
        while i < len(num1) and j < len(num2):
            if int(num1[i]) + int(num2[j]) + remainder == 0:
                ans.append('0')
                remainder = 0
            elif int(num1[i]) + int(num2[j]) + remainder == 1:
                ans.append('1')
                remainder = 0
            elif int(num1[i]) + int(num2[j]) + remainder == 2:
                ans.append('0')
                remainder = 1
            else:
                ans.append('1')
                remainder = 1
            i +=  1
            j += 1
        while i < len(num1):
            if int(num1[i]) + remainder == 2:
                ans.append('0')
                remainder = 1
            elif int(num1[i]) + remainder == 1:
                ans.append('1')
                remainder = 0
            else:
                ans.append('0')
                remainder = 0
            i += 1
        while j < len(num2):
            if int(num2[j]) + remainder == 2:
                ans.append('0')
                remainder = 1
            elif int(num2[j]) + remainder == 1:
                ans.append('1')
                remainder = 0
            else:
                ans.append('0')
                remainder = 0
            j += 1
        if remainder:
            ans.append('1')
        return  "".join(reversed(ans))
        
        