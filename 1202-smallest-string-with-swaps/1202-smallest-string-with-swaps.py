class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        rank = [1]*n
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
                
            return parent[node]
        
        def union(node1,node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                p1, p2 = p2, p1
            parent[p1] = p2
            rank[p2] += rank[p1]
            
            
        for n1, n2 in pairs:
            union(n1,n2)
            
        d = defaultdict(list)
        
        for i in range(n):
            d[find(i)].append(s[i])
            
        for l in d.values():
            l.sort(reverse=True)
            
        ret = []
        
        for i in range(n):
            ret.append(d[find(i)].pop())
            
        return ''.join(ret)
                    
            
        
        