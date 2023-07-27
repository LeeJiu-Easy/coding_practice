# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        mid = (length // 2) + 1
        
        answer = ListNode()

        i = 1
        cur = head
        while cur:
            if i == mid:
                answer.next = cur
                break
            cur = cur.next

            i += 1
        
        return answer.next