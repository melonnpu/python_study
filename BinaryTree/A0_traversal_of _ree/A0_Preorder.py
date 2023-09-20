"""
树的前序遍历
1.递归
2.迭代
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归一

        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # 递归二
        # def preorder(root: Optional[TreeNode]):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        #
        # res = list()
        # preorder(root)
        # return res

        # 迭代 栈
        res = list()
        if not root:
            return res

        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res







