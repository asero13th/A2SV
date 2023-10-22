class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = {i : i for i in range(n)}
        rank = {i : 1 for i in range(n)}
        
        hashmap = defaultdict(list)
        
        for x, y, time in meetings:
            hashmap[time].append([x,y])

        hashmap = OrderedDict(sorted(hashmap.items()))
        
        graph[firstPerson] = 0
        rank[0] += rank[firstPerson]
        
        def find(x , parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]
        
        def union(x, y):
            px = find(x, graph)
            py = find(y, graph)
            
            if px != py:
                if px < py:
                    graph[py] = px
                    rank[px] += rank[py]
                else:
                    graph[px] = py
                    rank[py] += rank[px]
        for key in hashmap:
            for x, y in hashmap[key]:
                union(x, y)
            
            for x, y in hashmap[key]:
                if find(x, graph) != 0:
                    graph[x] = x

                if find(y, graph) != 0:
                    graph[y] = y
            
        ans = []
        for key, val in graph.items():
            if val == 0:
                ans.append(key)
        return ans
        
        
        
        
        
        