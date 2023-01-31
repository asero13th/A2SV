# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        n = length - n + 1
        
        if n == 1:
            return head.next
        index = 1
        node = head
        
        while node:
            if index + 1 == n:
                node.next = node.next.next
            node = node.next
            index += 1
        return head
            