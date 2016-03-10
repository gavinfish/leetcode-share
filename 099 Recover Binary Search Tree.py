'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.node1 = None
        self.node2 = None
        self.pre = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.__scan(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val

    def __scan(self, root):
        if root is None:
            return
        self.__scan(root.left)
        if self.pre is not None:
            if root.val < self.pre.val:
                if self.node1 is None:
                    self.node1 = self.pre
                    self.node2 = root
                else:
                    self.node2 = root
        self.pre = root
        self.__scan(root.right)


if __name__ == "__main__":
    None