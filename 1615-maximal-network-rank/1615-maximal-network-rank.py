class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        def adjList(edges):
            graph = defaultdict(list)
            
            for i, j in edges:
                graph[i].append(j)
                graph[j].append(i)
            return graph
        adjList = adjList(roads)
        maximum = 0
        for key in adjList:
            for inner in adjList:
                if inner!= key and maximum < len(adjList[key]) + len(adjList[inner]):
                    maximum =  len(adjList[key]) + len(adjList[inner])
                    
                    if inner in adjList[key]:
                        maximum -= 1
        return maximum
                        

            
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def adjecencyList(matrix):
#             hashmap = defaultdict(list)
#             for key, val in matrix:
#                 hashmap[key].append(val)
#                 hashmap[val].append(key)
#             return hashmap
#         adjList = adjecencyList(roads)
#         maximum = 0
#         for key in adjList:
#             for inner in adjList:
#                 if inner!= key and maximum < len(adjList[key]) + len(adjList[inner]):
#                     maximum =  len(adjList[key]) + len(adjList[inner])
                    
#                     if inner in adjList[key]:
#                         maximum -= 1
#         return maximum
                        
            
        
        