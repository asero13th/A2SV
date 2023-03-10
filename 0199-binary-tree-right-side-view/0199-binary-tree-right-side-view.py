# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        hashmap = defaultdict(list)
        ans =[]
        def track(root, level):
            if not root:
                return 
            
            hashmap[level].append(root.val)
            track(root.right,level + 1)
            track(root.left, level + 1)
            
        track(root, 0)
        maximum_len = 0

        for arr in hashmap.values():
            ans.append(arr[0])
      
        return ans
        
        