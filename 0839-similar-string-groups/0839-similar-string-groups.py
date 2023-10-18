class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        graph = {i : i for i in range(len(strs))}
        rank = {i : 1 for i in range(len(strs))}
        
        def find(x , parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]
        
        def union(x, y):
            px = find(x, graph)
            py = find(y, graph)
            
            if px != py:
                if rank[px] > rank[py]:
                    graph[py] = px
                    rank[px] += rank[py]
                else:
                    graph[px] = py
                    rank[py] += rank[px]
        
            
            
        def check(str1, str2):
            if len(str1) > len(str2) or len(str2) > len(str1):
                return False
            
            i, c = 0,0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    c += 1
                    
            return c <= 2
        for i in range(len(strs)):
                for j in range(i):
                    if check(strs[i], strs[j]):
                        union(i, j)
        for i in range(len(strs)):
            find(i, graph)
            
        return len(Counter(graph.values()))
        
            
           
                    
        
                     
                    
            
            
        