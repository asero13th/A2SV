class Solution(object):
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0

   
        def dist(u, v):
            x1, y1 = points[u]
            x2, y2 = points[v]
            return abs(x1 - x2) + abs(y1 - y2)
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                p = parent[p]
            return p
        
        def union(u, v):
            p1 = find(u)
            p2 = find(v)
            
            # cycle found
            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return False

        n = len(points)
        edge_weight_map = defaultdict(int)
    
        for i in range(0, n):
            for j in range(i + 1, n):
                edge_weight_map[(i, j)] = dist(i, j)

      
        sorted_edges_list = sorted(edge_weight_map.items(), key = lambda x : x[1])

        parent = [i for i in range(0, n)]
        rank = [1 for _ in range(0, n)]
        
        cost = 0
        edges_count = 0
        
        # Find mst using Kruskal's algo
        for edge, weight in sorted_edges_list:
            u, v = edge
            
            if not union(u, v):
                cost += weight
                edges_count += 1
          
            if edges_count == n - 1:
                return cost
    