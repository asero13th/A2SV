from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
		result = 0
		def dfs(ind,last = -1):
		    nonlocal result
		    if result == 1: return
		    visited.add(ind)
		    for itr in adj[ind]:
		        if itr == last:
		            continue
		        if itr in visited:
		            result = 1
		            return 
		        dfs(itr,ind)
		for i in range(V):
		    if i not in visited:
		        dfs(i)
    		    if result == 1:
    		        return 1
		return 0
		        




#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends