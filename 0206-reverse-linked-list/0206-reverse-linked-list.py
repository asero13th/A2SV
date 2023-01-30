# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        arr = []
        while itr:
            arr.append(itr.val) 
            itr = itr.next
        
        arr.reverse()
        i = 0
        itr = head
        while itr:
            itr.val = arr[i]
            itr = itr.next
            i += 1
        return head
        