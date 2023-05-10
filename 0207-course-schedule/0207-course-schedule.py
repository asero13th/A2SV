class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        color = defaultdict(int)
        
        for course, pre in prerequisites:
            graph[course].append(pre)
        ans = []   
        def dfs(node):
            if color[node] == 1:
                return False
            
            if color[node] == 2:
                return True
            
            color[node] = 1
            for val in graph[node]:
                
                if not dfs(val):
                    return False
            
            color[node] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                
            

            
        
        
        