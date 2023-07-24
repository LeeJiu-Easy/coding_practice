# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()
        answer = False
        while head:
            if head in visit:
                answer = True
                break
            visit.add(head)
            head = head.next
        return answer