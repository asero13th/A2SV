class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def getAdjencyList(arr):
            hashmap = defaultdict(list)
            
            for n, m in edges:
                hashmap[n].append(m)
                hashmap[m].append(n)
            return hashmap
        
        graph = getAdjencyList(edges)
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            
            for val in graph[node]:
                if val not in visited and  dfs(val):
                    return True
            return False
        return dfs(source)
                
                
            
        