# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tmp = head
        counter = 1
        while tmp.next:
            if counter % 2 != 0:
                tmp.val, tmp.next.val  = tmp.next.val, tmp.val
            tmp = tmp.next
            counter += 1
        return head
            
        
        