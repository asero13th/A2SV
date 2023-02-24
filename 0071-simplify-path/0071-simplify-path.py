class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        patharr = path.split('/')
        
        print(patharr)
        for char in patharr:
            if stack and char == "..":
                stack.pop()
                
            elif char and char != '.' and char != '..':
                stack.append(char)
        ans = "/".join(stack)
            
        return '/' + ans
            
            
            
        