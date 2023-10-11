class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        map = {}
        res = set()
        def check(node):
            if not node:
                return '#'
            s = ''
            if not node.left and not node.right:
                s += str(node.val)
                map[s] = map.get(s,0)+1
                if map[s]==2:
                    res.add(node)
                return s
                
            s  = s + str(node.val)
            s = s + "," + check(node.left)
            s = s+ "," + check(node.right)

            map[s]  = map.get(s,0)+1
            if map[s]==2:
                res.add(node)
            return s
        
        check(root)
        return res