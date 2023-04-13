"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def adj(matrix):
            graph = defaultdict(list)
            sub = defaultdict(int)
            for employee in matrix:
                graph[employee.id] = employee.subordinates
                sub[employee.id] = employee.importance
            return [graph, sub]
        
        graph, importance = adj(employees)
        ans = 0
        visited = set()
        def dfs(vertex):
            nonlocal ans
            
            visited.add(vertex)
            ans += importance[vertex]
            for val in graph[vertex]:
                if val not in visited:
                    dfs(val)
        dfs(id)
        return ans
            