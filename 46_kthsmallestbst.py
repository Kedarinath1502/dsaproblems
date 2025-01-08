'''
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        def inorder_traverse(root: Optional[TreeNode]):
            nonlocal k, result
            if not root:
                return
            inorder_traverse(root.left)
            k -= 1
            if k == 0:
                result = root.val
            inorder_traverse(root.right)
        inorder_traverse(root)
        return result
    
