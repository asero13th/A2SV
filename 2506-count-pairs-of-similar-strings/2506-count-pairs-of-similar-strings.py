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
            
        
    def factorial(self,num):
        if num == 0:
            return 1
        else:
            return num * self.factorial(num - 1)
    def permutation(self,m):
        numerator = (m * (m - 1)) // 2
        
        return numerator
        