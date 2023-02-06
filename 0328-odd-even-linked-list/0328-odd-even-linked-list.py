# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        odd = ListNode()
        
        evenpointer = even
        oddpointer = odd
        node = head
        idx = 0
        
        while node:
            if idx % 2 == 0:
                evenpointer.next = ListNode(node.val,None)
                evenpointer = evenpointer.next
            else:
                oddpointer.next = ListNode(node.val,None)
                oddpointer = oddpointer.next
            node = node.next
            idx += 1
        evenpointer.next = odd.next
        return even.next
                
        