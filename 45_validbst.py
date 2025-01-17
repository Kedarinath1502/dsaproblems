'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, low, high):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return (validate(root.left, low, root.val) and
                    validate(root.right, root.val, high))
        return validate(root, float('-inf'), float('inf'))