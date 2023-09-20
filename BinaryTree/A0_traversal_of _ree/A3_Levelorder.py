from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            current_list = []
            for i in range(size):
                node = queue.pop(0)
                current_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_list)
        return res


"""
总结：
    树的前中后序遍历 深度优先搜索 栈
    层次遍历 广度优先搜索 队列
    
    延伸：
    广度优先搜索 无权最短路径问题
    Dijkstra 算法解决的是带权最短路径问题
"""