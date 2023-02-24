class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if stack and char in p and p[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0