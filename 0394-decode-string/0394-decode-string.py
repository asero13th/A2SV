class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = []
        if s.isdigit():
            return ""
        for idx, char in enumerate(s):
            if char.isdigit():
                if idx > 0 and s[idx - 1].isdigit():
                    num = str(stack.pop()) + char
                    stack.append(int(num))
                else:
                    stack.append(int(char))
            elif char == ']':
                nested = []
                while stack[-1] != '[':
                    nested.append(stack.pop())
                stack.pop()
                nested = stack.pop() * nested
                while nested:
                    stack.append(nested.pop())
            else:
                stack.append(char)
                
                
          
        return "".join(stack) if stack else ""
        
                
                            
                             
                             
                
                
                
            
        