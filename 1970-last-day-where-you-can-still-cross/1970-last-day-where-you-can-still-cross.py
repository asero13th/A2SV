class UnionFind: 
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p]) # find w/ path compression 
        return self.parent[p]
    
    def union(self, p, q): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False # already connected 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt # union by rank 
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 
    

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        grid = [[0]*col for _ in range(row)]
        
        n = row * col
        uf = UnionFind(n)
        span = [[n, 0] for _ in range(n)]
        
        for step, (i, j) in enumerate(cells): 
            i, j = i-1, j-1
            grid[i][j] = 1
            x = i*col + j
            for ii, jj in (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1): 
                if 0 <= ii < row and 0 <= jj < col and grid[ii][jj]: 
                    xx = ii*col + jj 
                    r, rr = uf.find(x), uf.find(xx)
                    span[r][0] = span[rr][0] = min(span[r][0], span[rr][0], j, jj)
                    span[r][1] = span[rr][1] = max(span[r][1], span[rr][1], j, jj)
                    if span[r] == [0, col-1]: return step 
                    uf.union(x, xx)