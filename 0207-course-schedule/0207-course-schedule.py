class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = defaultdict(int)
        graph = defaultdict(list)
        
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            degree[course] += 1
            
        queue = deque()
        for c in range(numCourses):
            if degree[c] == 0:
                queue.append(c)
        ans = []       
        while queue:
            
            node = queue.popleft()
            ans.append(node)
            for neigh in graph[node]:
                degree[neigh] -= 1
                
                if degree[neigh] == 0:
                    queue.append(neigh)
                    
        return len(ans) == numCourses
        