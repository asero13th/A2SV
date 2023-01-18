class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        ans = []
        
        for i, val in enumerate(arr):
            if stack:
                while stack and stack[-1][0] < val:
                    stack.pop()                                     
            stack.append([val,i])
        for i in range(stack[0][1]):
            ans.append(stack[0][0])
            
        for i,val in enumerate(stack):
            if i != 0:
                for j in range(stack[i - 1][1],stack[i][1]):
                    ans.append(val[0])
        ans.append(-1)
        return ans
        
        