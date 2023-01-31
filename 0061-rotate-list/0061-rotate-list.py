# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        
        length = 0
        tmp = head
        
        while tmp:
            length += 1
            tmp = tmp.next
            
        if length <= 1 or k % length == 0:
            return head
        
        k = (k % length)
        k = length - k + 1
        node = head
        index = 1
        current  = head
        
        while node:
            if index + 1 == k:
                current = node.next
                node.next = None
                break
            index += 1
            node = node.next
    
        tmp = current
        while tmp.next:
            tmp = tmp.next
        tmp.next = head
        
        return current