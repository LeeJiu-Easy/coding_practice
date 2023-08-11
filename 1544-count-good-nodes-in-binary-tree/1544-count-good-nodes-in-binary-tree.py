# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque

        q = deque([(root, [root.val])])

        answer = 0

        while q:
            cur, path = q.popleft()

            if cur.val >= max(path):
                answer += 1

            if cur.left:
                new_path = path + [cur.left.val]
                q.append((cur.left, new_path))
            
            if cur.right:
                new_path = path + [cur.right.val]
                q.append((cur.right, new_path))

        return answer