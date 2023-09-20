# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.rserialize(root, "")

    def rserialize(self, root: Optional[TreeNode], astr: str) -> str:
        if not root:
            astr += "None,"
        else:
            astr += str(root.val)+","
            astr = self.rserialize(root.left, astr)
            astr = self.rserialize(root.right, astr)
        return astr

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        datalist = data.split(",")
        print("datalist:", datalist)
        return self.rdeserialize(datalist)

    def rdeserialize(self, datalist: list):
        if datalist[0] == "None":
            datalist.pop(0)
            return None
        root = TreeNode(int(datalist[0]))
        datalist.pop(0)
        root.left = self.rdeserialize(datalist)
        root.right = self.rdeserialize(datalist)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
