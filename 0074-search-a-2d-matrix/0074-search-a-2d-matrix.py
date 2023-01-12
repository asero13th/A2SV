class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            if target <= mat[-1]:
                if target in mat:
                    return True
        return False