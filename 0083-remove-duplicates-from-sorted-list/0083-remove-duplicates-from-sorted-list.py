# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        nums = set()
        node = head
        tmp = new_node
        
        while node:
            if node.val not in nums:
                tmp.next = ListNode(node.val,None)
                tmp = tmp.next
            nums.add(node.val)
            node = node.next
        return new_node.next 
            
                
            
        