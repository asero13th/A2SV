class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def adjecencyList(matrix):
            occupied = [0] * n
            hashmap = defaultdict(list)
            for key, val in matrix:
                occupied[val] = 1
            return occupied
        ans = adjecencyList(edges)
      
        return [i for i,val in enumerate(ans) if val == 0 ]
        