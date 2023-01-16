class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        i = 0
        for row in zip(*(matrix)):
            matrix[i] = reversed(row)
            i += 1
           
            
        
        
    
        