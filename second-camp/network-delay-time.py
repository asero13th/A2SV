class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        def adjList():
            graph = defaultdict(list)

            for x, y ,z in times:
                graph[x].append((y, z))
            
            return graph
        graph = adjList()

        heap = [(0, k)]
        visited = set()
        distances = defaultdict(int)
        for node in range(1, n + 1):
            distances[node] = float("inf")
        distances[k] = 0
        
        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue
            
            visited.add(curr_node)

            for neigh, weight in graph[curr_node]:
                distance = curr_distance + weight

                if distance <  distances[neigh]:
                    distances[neigh] = distance
                    heapq.heappush(heap, (distance, neigh))

        print(distances, visited)
        ans = max(distances.values())
        return -1 if ans == float("inf") else ans

        

        