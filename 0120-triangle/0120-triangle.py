class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        store = defaultdict(int)
        def dp(l,m):
            
            for i in range(len(triangle) - 1,-1,-1):
                for j in range(len(triangle[i])):
                    store[(i, j)] = min(store[(i + 1, j)] , store[(i+ 1, j + 1)]) + triangle[i][j]
                
            return store[(l,m)]
        return dp(0,0)