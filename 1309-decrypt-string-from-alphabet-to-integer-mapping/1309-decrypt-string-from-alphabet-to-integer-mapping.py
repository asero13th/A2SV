class Solution:
    def freqAlphabets(self, s: str) -> str:
        val = 1
        hashmap = {}
        ans = ""
        stack = []

        for x in range(97, 122+1):
            hashmap[val] = chr(x)
            val += 1
        
        for char in s:
            if char.isdigit():
                stack.append(char)
            else:
                tmp = stack.pop() + stack.pop()
                tmp = tmp[::-1]
                stack.append(tmp)
        for num in stack:
            ans += hashmap[int(num)]
        return ans
                
                
            
                
            
        
            
        
        
        