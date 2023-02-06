# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            innernode = node
            val = node.val
            tmp = node
            while innernode:
                if val > innernode.val:
                    val = innernode.val
                    tmp = innernode
                innernode = innernode.next
            node.val,tmp.val = tmp.val,node.val
            node = node.next
        return head
                    
        