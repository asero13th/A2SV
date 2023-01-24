class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmap = {}
        colmap = {}
        for a in range(0,9,3):
            for b in range(0,9,3):
                hashmap = set()
                for i in range(a,a + 3):
                    for j in range(b, b + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in hashmap:
                            return False
                        
                        if i in rowmap:
                            if board[i][j] in rowmap[i]:
                                return False
                            rowmap[i].append(board[i][j])
                            
                        else:
                            rowmap[i] = [board[i][j]]
                            
                        if j in colmap:
                            if board[i][j] in colmap[j]:
                                return False
                            colmap[j].append(board[i][j])
                        else:
                            colmap[j] = [board[i][j]]
                            
                        hashmap.add(board[i][j])
                
                    
        return True