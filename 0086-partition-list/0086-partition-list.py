# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthanx = ListNode()
        greaterthanx = ListNode()
        node = head
        
        itr1 = lessthanx
        itr2 = greaterthanx
        while node:
            if node.val < x:
                itr1.next = ListNode(node.val,None)
                itr1 = itr1.next
            else:
                itr2.next = ListNode(node.val,None)
                itr2 = itr2.next
            node = node.next
            
        itr1.next = greaterthanx.next

        
        
        return lessthanx.next