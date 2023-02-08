# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for head in lists:
            while head:
                ans.append(head.val)
                head = head.next
        ans.sort()
        dummy = ListNode()
        reference = dummy
        for num in ans:
            reference.next = ListNode(num,None)
            reference = reference.next
        return dummy.next
        