class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        tmp = (zip(*(matrix)))
        i = 0
        for row in tmp:
            matrix[i] = reversed(row)
            i += 1
        print(matrix)
           
            
        
        
    
        