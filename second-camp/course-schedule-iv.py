class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def adjList():
            graph = defaultdict(list)
            level = defaultdict(int)
            
            for pre, course in prerequisites:
                graph[pre].append(course)
                level[pre] += 1
            
            return [graph, level]
        graph, level = adjList()
        matrix = [[False for i in range(numCourses)] for j in range(numCourses)]
        def dfs(i, j):
            nonlocal boolean
            for neigh in graph[i]:
                if neigh == j:
                    boolean =  True
                if neigh not in visited:
                    visited.add(neigh)
                    
                    dfs(neigh, j)
                
            return boolean
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                visited = set()
                boolean = False
                matrix[i][j] = dfs(i, j)
    
        ans = []
        for x, y in queries:
            ans.append(matrix[x][y])
            
        return ans
        
#         queue = deque()
#         for i in range(numCourses):
#             if level[i] == 0:
#                 queue.append(i)
#         print(graph) 
#         while queue:
            
#             course = queue.popleft()
            
#             for neigh in graph[course]:
#                 level[neigh] -= 1
#                 matrix[course][neigh] = True
                
#                 if level[neigh] == 0:
#                     queue.append(neigh)
                    
#         ans = []
#         for x, y in queries:
#             ans.append(matrix[y][x])
#         return ans
        
            
            
        