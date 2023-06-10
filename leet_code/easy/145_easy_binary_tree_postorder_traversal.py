#Input: root = [1,null,2,3]
#Output: [3,2,1]

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def postorder(node):
            if node == None:
                return
            postorder(node.left)
            postorder(node.right)
            answer.append(node.val)
            return answer
        return postorder(root)
