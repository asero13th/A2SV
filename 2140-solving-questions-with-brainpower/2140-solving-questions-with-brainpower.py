class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        store = defaultdict(int)
        def dp(i):
           
            
            if i >= len(questions):
                return 0
            
            nextt = questions[i][1]
            val = questions[i][0]
            
            if i not in store:
                store[i] = max(val + dp(i + (nextt + 1)), dp(i + 1))
            
            return store[i]
        return dp(0)