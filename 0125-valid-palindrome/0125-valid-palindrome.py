class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for char in s:
            if char.isalpha():
                ans.append(char.lower())
            if char.isdigit():
                ans.append(char)
       
        return ans == ans[len(ans) -1::-1]
        