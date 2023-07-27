# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        binary_num = ""
        
        while cur:
            binary_num += str(cur.val)
            cur = cur.next

        answer = 0
        for i, string in enumerate(binary_num[::-1]):
            if string == '1':
                answer += 2**i

        return answer