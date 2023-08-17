class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        store = defaultdict(int)
        def dp(j):
            prev = 0
            for i in range(len(questions) - 1, -1, -1):
                val = questions[i][0]
                nextt = questions[i][1]
                store[i] = max(val + store[i  + 1 + nextt], store[i + 1])
                
                
                
            return store[j]
        return dp(0)