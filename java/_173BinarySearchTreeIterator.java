import java.util.Stack;

/**
 * Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
 * Calling next() will return the next smallest number in the BST.
 * <p>
 * Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
 * <p>
 * Credits:
 * Special thanks to @ts for adding this problem and creating all test cases.
 * <p>
 * Created by drfish on 6/8/2017.
 */
public class _173BinarySearchTreeIterator {
    public class BSTIterator {
        private Stack<TreeNode> stack;
        private TreeNode node;

        public BSTIterator(TreeNode root) {
            stack = new Stack<>();
            node = root;
        }

        /**
         * @return whether we have a next smallest number
         */
        public boolean hasNext() {
            return node != null || !stack.isEmpty();
        }

        /**
         * @return the next smallest number
         */
        public int next() {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            TreeNode temp = stack.pop();
            node = temp.right;
            return temp.val;
        }
    }
}
