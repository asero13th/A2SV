class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        oneD = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]
        ans = []
        k = 0

        for i in range(r):
            tmp = []
            for j in range(c):
                tmp.append(oneD[k])
                k += 1
            ans.append(tmp)
            
        return ans
                
                
                
            
        
        
        
        
        