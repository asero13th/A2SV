class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def adjList(matrix):
            hashmap = defaultdict(list)
            
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 1:
                        hashmap[j + 1].append(i + 1)
            return hashmap
        hashmap = adjList(isConnected)
        visited = set()
        
        
        def dfs(vertex):
            
            visited.add(vertex)
            for neighbour in hashmap[vertex]:
                if neighbour not in visited:
                    dfs(neighbour)
            return 1
        
        ans = 0
        for val in hashmap:
            if val not in visited:
                ans += dfs(val)
        return ans
                    
                    
                    
                
            
        