class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        hashmap = {}
        i,j = 0,0
        ans = []
        
        while len(matrix) * len(matrix[0]) > len(hashmap):
            for x,y in direction:
                if (i,j) in hashmap:
                    i = i + x
                    j = j + y
                    
                while (i,j) not in hashmap  and 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                    hashmap[(i,j)] = matrix[i][j]
                    ans.append(matrix[i][j])
                    i += x
                    j += y
                
                i = i - x
                j = j - y
        return ans
                    
                    
                    
                    
                    
                    
                    
            