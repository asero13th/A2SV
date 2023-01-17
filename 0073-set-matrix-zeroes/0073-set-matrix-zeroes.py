class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        row,col =set(),set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row or j in col:
                    matrix[i][j] = 0
        return matrix
        
        