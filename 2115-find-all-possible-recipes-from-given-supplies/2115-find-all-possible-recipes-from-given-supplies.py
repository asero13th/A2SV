class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply = set(supplies)
        graph = defaultdict(list)
        degree = defaultdict(int)
        queue = deque()
        for idx,food in enumerate(recipes):
            for values in ingredients[idx]:
                if values not in supply:
                    graph[values].append(food)
                    degree[food] += 1
                    
            if degree[food] == 0:
                queue.append(food)
        
                
        ans = []     
        while queue:
            
            node =  queue.popleft()
            ans.append(node)
            
            for neigh in graph[node]:
                degree[neigh] -= 1
                
                if degree[neigh] == 0:
                    queue.append(neigh)
                    
        return ans
            
            
        
            
        
        