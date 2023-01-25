class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        wordcount = Counter(s)
        charset = set()
        word = []
        ans = []
        for char in s:
            wordcount[char] -= 1
            
            if char not in charset:
                charset.add(char)
            word.append(char)
                
            if wordcount[char] == 0:
                charset.remove(char)
                
            if len(charset) == 0:
                ans.append(len(word))
                word = []
        return ans
                
                
            
            
        