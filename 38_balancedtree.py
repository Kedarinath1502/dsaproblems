'''
Given a binary tree, determine if it is height-balanced.
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return dfs(root) != -1
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.balanced = False
            return 1 + max(left, right)
        dfs(root)
        return self.balanced