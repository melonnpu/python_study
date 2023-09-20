from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
树的两种递归方法
自顶向下：根据根结点数据->算自节点
自底向上：根据子节点数据->算根结点
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # 方法一：递归 自底向上
        # if not root:
        #     return 0
        # leftMax = self.maxDepth(root.left)
        # rightMax = self.maxDepth(root.right)
        # return max(leftMax,rightMax)+1

        # 递归：自顶向下
        res = 0

        def maxDepth2(root: Optional[TreeNode], depth: int):
            nonlocal res
            if not root:
                return
            if not root.left and not root.right:
                res = max(res, depth)
            maxDepth2(root.left, depth + 1)
            maxDepth2(root.right, depth + 1)

        maxDepth2(root, 1)
        return res


        # 方法二：迭代
        # if not root:
        #     return 0
        # queue = [root]
        # depth = 0
        #
        # while queue:
        #     for i in range(len(queue)):
        #         r = queue.pop(0)
        #         if r.left:
        #             queue.append(r.left)
        #         if r.right:
        #             queue.append(r.right)
        #     depth += 1
        #
        # return depth


