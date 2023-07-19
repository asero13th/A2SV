class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)
        for x,y in dislikes:
            g[x].append(y)
            g[y].append(x)
        
        color = {}
        
        def dfs(i, c):
            color[i] = c
            for enemy in g[i]:
                if enemy in color:
                    # if enemy has same color, then return False directly
                    if color[enemy]==c:
                        return False
                else:
                    # assign inverted color to enemy and check for anomalies
                    if not dfs(enemy, 1-c):
                        return False
            return True
            
        for i in range(1, n+1):
            if i not in color:
                # assign color 1 and check for anomalies
                if not dfs(i, 1):
                    return False
         
		 # We found no anomaly, so return True
        return True
        