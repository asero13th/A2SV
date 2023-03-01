# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        cpnode = node
        
        self.compare(list1, list2, node)
        return cpnode.next
    
    def compare(self, list1, list2,node):
        if not list1 and not list2:
            return
        
        if list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val,None)
                node = node.next
                self.compare(list1.next, list2, node)
            else:
                node.next = ListNode(list2.val,None)
                node = node.next
                self.compare(list1, list2.next, node)
        else:
            if list1:
                node.next = ListNode(list1.val,None)
                node = node.next
                self.compare(list1.next, list2, node)
            else:
                node.next = ListNode(list2.val,None)
                node = node.next
                self.compare(list1, list2.next, node)
            
        return node
        
        
        