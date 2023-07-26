#Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
#Input: head = [1,2,2,1]
#Output: true

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        val_str = ""
        while head:
            val_str += str(head.val)
            head = head.next
        if val_str == val_str[::-1]:
            return True
        else:
            return False