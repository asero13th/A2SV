# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        array = []
        def pick(root, arr):
            nonlocal array
            if not root:
                return
            if not root.right and not root.left:
                array.append(arr)
            
            arr.append(str(root.val))
            
            pick(root.left, arr.copy())
            pick(root.right, arr.copy())
            
            
            return
            
        pick(root,[])
        for idx,string in enumerate(array):
            array[idx] = ("->").join(string)
        return array
            
            
            
            
            
            
        