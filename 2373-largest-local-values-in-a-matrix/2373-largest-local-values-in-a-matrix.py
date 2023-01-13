class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(grid) - 2):
            tmp = []
            for j in range(len(grid[i]) - 2):
                maximum = 1
                
                for l in range(i,i + 3):
                    for k in range(j,j + 3):
                        maximum = max(maximum, grid[l][k])
                tmp.append(maximum)
            ans.append(tmp)
        return ans
                    
                
                
                    
                    
        