class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap_row = {}
        hashmap_col = {}
        ans = 0
        for row in grid:
            tmp = tuple(row)
            hashmap_row[tmp] = hashmap_row.get(tmp, 0) + 1
        
        column = zip(*(grid))
        for col in column:
            hashmap_col[col] = hashmap_col.get(col, 0) + 1
        for row in hashmap_row:
            if row in hashmap_col:
                ans =ans + (hashmap_col[row] * hashmap_row[row]) 
        return ans
            
                