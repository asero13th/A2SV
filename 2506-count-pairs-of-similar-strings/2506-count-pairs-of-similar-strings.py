class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hashmap = {}
        ans = 0
        
        for word in words:
            c = list(set(word))
            c.sort()
            c = "".join(c)
            hashmap[c] = hashmap.get(c,0) + 1
            
        for word in hashmap:
            num = hashmap[word]
            ans += self.permutation(num) if num > 1 else 0
        return ans
            
        
    def permutation(self,m):
        return (m * (m - 1)) // 2
    
        