class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        x = 0
        for i in tokens:
            if i in "+/*-":
                if i == '+':
                    x = (stack.pop() + stack.pop())
                    stack.append(x)
                if i == '/':
                    x = (stack.pop(len(stack) - 2) / stack.pop())
                    stack.append(int(x))
                if i == '-':
                    x = - (stack.pop() - stack.pop())
                    stack.append(x)
                if i == '*':
                    x = (stack.pop() * stack.pop())
                    stack.append(x)
            else:
                stack.append(int(i))
            
        return stack[0]
            
        