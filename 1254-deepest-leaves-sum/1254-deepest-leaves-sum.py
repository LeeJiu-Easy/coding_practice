# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        q = deque([(root, 0)])
        answer = 0
        visit_level = 0
        while q:
            cur, level = q.popleft()
            level += 1

            if cur.left:
                q.append((cur.left, level))
            
            if cur.right:
                q.append((cur.right, level))
            
            if not cur.left and not cur.right:
                if visit_level < level:
                    answer = cur.val
                elif visit_level == level:
                    answer += cur.val
            visit_level = level

        return answer