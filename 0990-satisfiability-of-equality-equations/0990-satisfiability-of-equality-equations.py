class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(str)
        rank = defaultdict(int)
        
        
        for val in equations:
            a = val[0]
            b = val[-1]
            graph[a], rank[a] = a, 1
            graph[b], rank[b] = b, 1
            
            
        def unionFind(x):
            if graph[x] == x:
                return x
            
            val = unionFind(graph[x])
            graph[x] = val
            return val
        def solve(arr):
            start = 1
            last =len(arr[0]) - 1
            for val in equations:
                if val[1:3] == "==":
                    edge1 = unionFind(val[0])
                    edge2 = unionFind(val[3])
                    
                    if rank[edge1] > rank[edge2]:
                        graph[edge2] = graph[edge1]
                        rank[edge1] += rank[edge2]
                        
                    else:
                        graph[edge1] = graph[edge2]
                        rank[edge2] += rank[edge1]
            for val in equations:
                if val[1:3] == "!=":
                    if unionFind(val[0]) == unionFind(val[3]):
                        return False
            return True
        return solve(equations)
                    
                    
                    
                    
                
                
            