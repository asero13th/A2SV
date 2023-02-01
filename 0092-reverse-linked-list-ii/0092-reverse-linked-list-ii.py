# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        tmp = ListNode()
        new_node = tmp
        node = head
        index = 1
        while node:
            if left <= index <= right:
                new_node.next = ListNode(node.val,None)
                new_node = new_node.next
            if index > right:
                break
            node = node.next
            index += 1
        reversed_node = self.reverseList(tmp.next)
        leftnode = head
        index = 0
        while leftnode.next and index + 1 < left - 1:
            leftnode = leftnode.next
            index += 1
        leftnode.next = reversed_node
        while reversed_node.next:
            reversed_node = reversed_node.next
        reversed_node.next = node
        return head if left > 1 else head.next
            
        
            
        
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,c = None, head
        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
        return p