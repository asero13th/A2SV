class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        store = defaultdict(int)
        def dp(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            
            if (i,j) not in store:
                store[(i, j)] = min(dp(i + 1, j) , dp(i+ 1, j + 1)) + triangle[i][j]
                
            return store[(i, j)]
        return dp(0,0)