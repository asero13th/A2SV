class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        digit = k
        for char in s:
            if stack and stack[-1][0] == char:
                stack.append((char, stack[-1][1] + 1))
            else:
                stack.append((char, 1))
            
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
        ans = []
        for char, count in stack:
            ans.append(char)
        return "".join(ans)
            
            

            
        