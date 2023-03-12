# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashmap = defaultdict(int)
        
        def nodes(node):
            if not node:
                return 

            hashmap[node.val] += 1
            nodes(node.left)
            nodes(node.right)
            
        nodes(root)
        ans = []
        maximum = root.val
      
        for val in hashmap:
            if hashmap[val] > hashmap[maximum]:
                ans = [val]
                maximum = val
            elif hashmap[val] == hashmap[maximum]:
                ans.append(val)
                
            
        return ans