# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tmp  = head
        length = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverseList(slow)
        ans = 0
        while rev and head:
            ans = max(ans,rev.val + head.val)
            head = head.next
            rev = rev.next
        return ans
            
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,c = None, head
        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        return p
        