class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def getLength(hash1, hash2):
            for val in hash1:
                if val in hash2:
                    return 0
                
            return sum(hash1.values()) * sum(hash2.values())
        def hashwords(words):
            ans = 0
            wordhash = []
            
            for word in words:
                wordhash.append(Counter(word))
                
            return wordhash
            
        def solve(words):
            maximum = 0
            for i in range(len(words)):
                for j in range(len(words)):
                    maximum = max(maximum, getLength(words[i], words[j]))
            return maximum
        return solve(hashwords(words))
        
                    
            
            
        
        
        