class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(str)
     
        for i in range(len(s1)):
            graph[s1[i]] = s1[i]
            graph[s2[i]] = s2[i]
           
            
        
        def unionFind(x):
            if graph[x] == x:
                return x
            
            val = unionFind(graph[x])
            graph[x] = val
            return val
        
        def solve():
            for i in range(len(s1)):
                edge1 = unionFind(s1[i])
                edge2 = unionFind(s2[i])
                
                if edge1 != edge2:
                    if edge1 > edge2:
                        graph[edge1] = edge2
                    else:
                        graph[edge2] = edge1
            ans = []
            for val in baseStr:
                word = unionFind(val)
                if word:
                    ans.append(word)
                else:
                    ans.append(val)
            return "".join(ans)
        return solve()
                
                    