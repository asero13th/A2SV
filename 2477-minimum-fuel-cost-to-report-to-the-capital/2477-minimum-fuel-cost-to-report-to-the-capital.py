class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(set)
        # find the adjacency list representation
        for i,j in roads:
            graph[i].add(j)
            graph[j].add(i)
        n = len(graph)
        if n==0: return 0
        visited = [False]*n
        self.ans = 0
        def dfs(city): 
        # return total number of representatives can be at city
        # and update answer self.ans for each city
            visited[city] = True
            repnum = 1 # initialize with 1 representative of city
            for neighbor in graph[city]:
                if not visited[neighbor]:
                    repnum += dfs(neighbor)
            if city==0: return None # do not update answer for capital
            self.ans += math.ceil(repnum/seats) # update answer
            return repnum
        dfs(0) # execute the DFS
        return self.ans
        