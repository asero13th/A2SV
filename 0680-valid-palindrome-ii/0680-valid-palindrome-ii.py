class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0,len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                str1 = s[:i] + s[i + 1:]
                str2 = s[:j] + s[j + 1:]
                if str1 == "".join(reversed(str1)):
                    return True
                elif str2 == "".join(reversed(str2)):
                    return True
                else:
                    return False
            i += 1
            j -= 1
        return True
            
        