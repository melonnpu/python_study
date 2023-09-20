"""
树的后序遍历
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # 递归解法一：
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


        # # 递归解法二：
        # res = []
        #
        # def postorder(root):
        #     if not root:
        #         return
        #     postorder(root.left)
        #     postorder(root.right)
        #     res.append(root.val)
        # postorder(root)
        # return res

        # 迭代:显示维护栈
        if not root:
            return []
        res = []
        stack = []
        prer = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prer:
                res.append(root.val)
                prer = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res
