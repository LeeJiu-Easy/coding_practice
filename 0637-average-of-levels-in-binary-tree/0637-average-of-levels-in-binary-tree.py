# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque, defaultdict, Counter

        q = deque([(root,0)])
        answer_dict = defaultdict(int)
        level_list = []

        while q:
            cur, level = q.popleft()
            
            answer_dict[level] += cur.val
            level_list.append(level)
        
            level += 1

            if cur.left:
                q.append((cur.left, level))
            if cur.right:
                q.append((cur.right, level))
        
        level_cnt = Counter(level_list)

        for level in level_cnt.keys():
            answer_dict[level] /= level_cnt[level]
             
        return list(answer_dict.values())