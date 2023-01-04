class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i):
                if set(words[i]) == set(words[j]):
                    count +=1
        return count
#         hashmap = {}
#         ans = 0
        
#         for word in words:
#             c = list(set(word))
#             c.sort()
#             c = "".join(c)
#             hashmap[c] = hashmap.get(c,0) + 1
            
#         for word in hashmap:
#             num = hashmap[word]
#             ans += self.permutation(num) if num > 1 else 0
#         return ans
            
        
#     def permutation(self,m):
#         return (m * (m - 1)) // 2
    
        