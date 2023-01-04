class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        i = 0
        for idx,char in enumerate(s):
            if i < len(spaces) and idx == spaces[i]:
                ans += " "
                i += 1
            ans += char
    
        return ans