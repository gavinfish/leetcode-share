'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Solve it recursively
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)

    # Solve it iteratively
    def isSymmetric_iterate(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack1, stack2 = [], []
        stack1.append(root.left)
        stack2.append(root.right)
        while stack1 and stack2:
            size1 = len(stack1)
            size2 = len(stack2)
            if size1 != size2:
                return False
            for __ in range(size1):
                curr1, curr2 = stack1.pop(), stack2.pop()
                if not curr1 and not curr2:
                    continue
                if not curr1 or not curr2:
                    return False
                if curr1.val != curr2.val:
                    return False
                stack1.append(curr1.left)
                stack1.append(curr1.right)
                stack2.append(curr2.right)
                stack2.append(curr2.left)
        return not stack1 and not stack2

if __name__ == "__main__":
    None