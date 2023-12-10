class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
      
        res = []

       
        def dfs(root):
            if root is None:
                return None
                
          
            root.left = dfs(root.left)
            root.right = dfs(root.right)


            if root.val in to_delete: 
               
                if root.left is None and root.right is None:
                    return None 
                else:
                   
                    if root.left:
                        res.append(root.left)
                    if root.right:
                        res.append(root.right)
                    return None
            
           
            return root
        

        to_delete = set(to_delete)
       
        node = dfs(root)
        if node:
            res.append(node)
        return res