class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        def adjecencyList(matrix):
            hashmap = defaultdict(list)
            for key, val in matrix:
                hashmap[key].append(val)
                hashmap[val].append(key)
            return hashmap
        
        adjList = adjecencyList(edges)

        for key in adjList:
            if len(adjList[key]) > 1:
                return key
        return -1
                
                    
                    
            
            
        