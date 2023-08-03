# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        q = deque([root])
        total = 0

        while q:
            cur = q.popleft()
    
            if cur.left:
                if not cur.left.left and not cur.left.right:
                    total += cur.left.val
                
                q.append(cur.left)
            
            if cur.right:
                q.append(cur.right)
            
        return total