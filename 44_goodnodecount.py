'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X 
there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, val):
            if not root:
                return
            if root.val >= val:
                self.count += 1
            dfs(root.left, max(root.val, val))
            dfs(root.right, max(root.val, val))
        dfs(root, min(root.val, float('-inf')))
        return self.count
    
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, val):
            if not root:
                return 0
            res = 1 if root.val >= val else 0
            res += dfs(root.left, max(root.val, val))
            res += dfs(root.right, max(root.val, val))
            return res
        return dfs(root, root.val)