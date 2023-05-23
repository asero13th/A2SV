class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(str)
        rank = defaultdict(int)
        for  i, account in enumerate(accounts):
            for  j, val in enumerate(account):
                if j > 0:
                    graph[val] = val
                    rank[val] = 1
        def unionFind(x):
                if graph[x] == x:
                    return x

                val = unionFind(graph[x])
                graph[x] = val
                return val
        def union(x, y):
                edge1 = unionFind(x)
                edge2 = unionFind(y)

                if edge2 != edge1:
                    if rank[edge1] > rank[edge2]:
                        rank[edge1] += rank[edge2]
                        graph[edge2] = graph[edge1]
                    else:
                        graph[edge1] = graph[edge2]
                        rank[edge2] += rank[edge1]
        for account in accounts:
            for i in range(1, len(account) - 1):
                x, y = account[i], account[i + 1]
                union(x, y)
        hashmap = defaultdict(list)
        for key, val in graph.items():
            x = unionFind(key)
            hashmap[x].append(key)
        ans = []  
        for account in accounts:
            for val in account:
                if val in hashmap:
                    tmp = [account[0]]
                    hashmap[val].sort()
                    tmp.extend(hashmap[val])
                    
                    if tmp not in ans:
                        ans.append(tmp)
        return ans
                
        
        
        
        
            

            
            
            
       