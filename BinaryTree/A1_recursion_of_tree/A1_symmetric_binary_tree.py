"""对称二叉树"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isTrue(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return isTrue(l.left, r.right) and isTrue(l.right, r.right)
            return False

        return isTrue(root, root)
