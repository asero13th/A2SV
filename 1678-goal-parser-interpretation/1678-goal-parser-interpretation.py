class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        ans =""
        for idx,letter in enumerate(command):
            if letter == "G":
                ans += letter
            elif letter == "(" and command[idx + 1] == ")":
                ans += 'o'
            elif letter == "(" and command[idx + 1] == "a":
                ans += 'al'
        return ans
            
        