class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = []
        for val in address:
            if val == '.':
                ans.append("[" + val + "]")
            else:
                ans.append(val)
        return "".join(ans)
        
        