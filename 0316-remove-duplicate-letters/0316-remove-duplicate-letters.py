class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        
        for char in s:
            while stack  and char not in stack and stack[-1] in counter and stack[-1] > char:
                stack.pop()
            if char not in stack:  
                stack.append(char)
            
            counter[char] -= 1
            if counter[char] == 0:
                counter.pop(char)
            
            
        return "".join(stack)
        