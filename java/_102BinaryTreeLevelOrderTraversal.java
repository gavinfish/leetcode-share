import java.util.ArrayList;
import java.util.List;

/**
 * Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
 * <p>
 * For example:
 * Given binary tree [3,9,20,null,null,15,7],
 *   3
 *  / \
 * 9  20
 *   /  \
 * 15   7
 * <p>
 * return its level order traversal as:
 * [
 *   [3],
 *   [9,20],
 *   [15,7]
 * ]
 * <p>
 * Created by drfish on 29/05/2017.
 */
public class _102BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        List<TreeNode> curr = new ArrayList<>();


        if (root == null) {
            return result;
        }
        curr.add(root);

        while (!curr.isEmpty()) {
            List<TreeNode> next = new ArrayList<>();
            List<Integer> level = new ArrayList<>();
            for (TreeNode node : curr) {
                if (node.left != null) {
                    next.add(node.left);
                }
                if (node.right != null) {
                    next.add(node.right);
                }
                level.add(node.val);
            }
            result.add(level);
            curr = next;
        }
        return result;
    }
}
