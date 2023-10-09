class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        def adjList():
            graph = defaultdict(list)

            for i, arr in enumerate(edges):
                x, y = arr
                graph[x].append((y,-1 * succProb[i]))
                graph[y].append((x, -1 * succProb[i]))

            return graph
        graph = adjList()
        distances = [float("inf") for node in range(n)]
        heap = [(start_node, 1)]
        visited = set()

        while heap:

            curr_node, curr_dist = heapq.heappop(heap)

            if curr_node in visited:
                continue

            for neigh, weight in graph[curr_node]:
                distance = curr_dist * weight
                if distance > 0:
                    distance = -1 * distance

                if distance < distances[neigh]:
                    distances[neigh] = distance
                    heapq.heappush(heap, (neigh, distance))
        print(distances)
        return -1 * distances[end_node] if distances[end_node] != float("inf") else 0