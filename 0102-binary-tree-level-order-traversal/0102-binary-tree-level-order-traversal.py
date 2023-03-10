# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        
        def track(root, level):
            if not root:
                return 
            
            hashmap[level].append(root.val)
            track(root.left,level + 1)
            track(root.right, level + 1)
            
        track(root, 0)
        return hashmap.values()
        
        