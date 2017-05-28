import java.util.Stack;

/**
 * Given a binary tree, determine if it is a valid binary search tree (BST).
 * <p>
 * Assume a BST is defined as follows:
 * The left subtree of a node contains only nodes with keys less than the node's key.
 * The right subtree of a node contains only nodes with keys greater than the node's key.
 * Both the left and right subtrees must also be binary search trees.
 * <p>
 * Example 1:
 *   2
 *  / \
 * 1   3
 * Binary tree [2,1,3], return true.
 * Example 2:
 *   1
 *  / \
 * 2   3
 * Binary tree [1,2,3], return false.
 * <p>
 * Created by drfish on 28/05/2017.
 */
public class _098ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        Stack<TreeNode> stack = new Stack<>();
        TreeNode prev = null;
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (prev != null && prev.val >= root.val) {
                return false;
            }
            prev = root;
            root = root.right;
        }
        return true;
    }
}
