"""
路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
如果存在，返回 true ；否则，返回 false 。
叶子节点 是指没有子节点的节点。

作者：LeetCode
链接：https://leetcode.cn/leetbook/read/data-structure-binary-tree/xo566j/
来源：力扣（LeetCode）
"""
from typing import Optional


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 解法一：累加
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     # 先接个深度遍历
    #     return self.hasPathSumHelper(root, 0, targetSum)
    #
    # def hasPathSumHelper(self, root: Optional[TreeNode], sum: int, targetSum: int) -> bool:
    #     if not root:
    #         return False
    #     sum += root.val
    #     if not root.left and not root.right and sum == targetSum:
    #         return True
    #     return self.hasPathSumHelper(root.left, sum, targetSum) or \
    #         self.hasPathSumHelper(root.right, sum, targetSum)

    # 解法二：累减
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)




