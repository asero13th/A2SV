class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        stackt = []
        
        for char in s:
            if char != "#": stacks.append(char)
            elif stacks: stacks.pop()
        for char in t:
            if char != "#": stackt.append(char)
            elif stackt: stackt.pop()
        
        return stacks == stackt