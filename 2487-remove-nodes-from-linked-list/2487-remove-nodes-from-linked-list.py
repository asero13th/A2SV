# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        head = self.reverseList(head)
        
        while head:
            if head.val >= node.val:
                node.next = ListNode(head.val,None)
                node = node.next
            head = head.next
        return self.reverseList(dummy.next)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,c = None, head
        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        return p
        