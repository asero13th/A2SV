"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root):
                
        
        
        
        if root is None:
            return 0
        
        maxDepthOfChildren = 0
        
        for child in root.children:
            depth = self.maxDepth(child)
            maxDepthOfChildren = max(maxDepthOfChildren, depth)
            
        return maxDepthOfChildren + 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
