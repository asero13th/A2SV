class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hashmap = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i -j in hashmap:
                    if not matrix[i][j] == hashmap[i - j]:
                        return False
                else:
                    hashmap[i - j] = matrix[i][j]
        return True
        