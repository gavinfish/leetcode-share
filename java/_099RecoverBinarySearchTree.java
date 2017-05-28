import java.util.Stack;

/**
 * Two elements of a binary search tree (BST) are swapped by mistake.
 * Recover the tree without changing its structure.
 * <p>
 * Note:
 * A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
 * <p>
 * Created by drfish on 28/05/2017.
 */
public class _099RecoverBinarySearchTree {
    public void recoverTree(TreeNode root) {
        TreeNode first = null;
        TreeNode second = null;
        TreeNode prev = null;
        Stack<TreeNode> stack = new Stack<>();
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (prev != null && prev.val >= root.val) {
                if (first == null) {
                    first = prev;
                }
                second = root;
            }
            prev = root;
            root = root.right;
        }
        swap(first, second);
    }

    private void swap(TreeNode node1, TreeNode node2) {
        int temp = node1.val;
        node1.val = node2.val;
        node2.val = temp;
    }
}
