# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str1 = ""
        str2 = ""
        
        while head:
            str1 = str(head.val) + str1
            str2 = str2 + str(head.val)
            
            head = head.next
            
        return True if str1 == str2 else False