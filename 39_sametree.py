'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have 
the same value.
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            nodeP = q1.popleft()
            nodeQ = q2.popleft()
            if nodeP is None and nodeQ is None:
                continue
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False
            q1.append(nodeP.left)
            q1.append(nodeP.right)
            q2.append(nodeQ.left)
            q2.append(nodeQ.right)
        return True