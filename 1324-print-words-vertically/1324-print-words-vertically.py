class Solution:
    def printVertically(self, s: str) -> List[str]:
        string_arr, maximum_word = s.split(),  0
        
        for word in string_arr:
            maximum_word = max(maximum_word,len(word))
            
        ans = [""] * maximum_word
        
        for i in range(maximum_word):
            tmp = []
            space = 0
            for j in range(len(string_arr)):
                if i < len(string_arr[j]):
                    if space:
                        spaces = " " * space
                        tmp.append(spaces)
                        space = 0
                    tmp.append(string_arr[j][i])
                    
                else:
                    space += 1
                        
            ans[i] = "".join(tmp)
        return ans
            
            
            