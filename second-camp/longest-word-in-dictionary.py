class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        print(words)
        def solve():
            ans = ""
            for word in words:
                for idx,char in enumerate(word):
                    if word[:idx + 1] not in words:
                        break
                
                else: 
                    if len(ans) < len(word):
                        ans = word
                    
            return ans
        
        return solve()

        