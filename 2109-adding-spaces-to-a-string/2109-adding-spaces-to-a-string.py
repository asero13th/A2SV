class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        if len(s) == 1:
            return " " + s
        
        if len(spaces) == 1:
            return s[:spaces[0]] + " " + s[spaces[0]:]
        
        answer = s[: spaces[0]] + " "
        for i in range(1, len(spaces)):
            left, right = spaces[i - 1], spaces[i]
            answer += s[left:right] + " "
        answer += s[right:]
        return answer
#         ans = ""
#         i = 0
#         for idx,char in enumerate(s):
#             if i < len(spaces) and idx == spaces[i]:
#                 ans += " "
#                 i += 1
#             ans += char
    
#         return ans