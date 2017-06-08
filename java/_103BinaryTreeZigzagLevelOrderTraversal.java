import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
 * <p>
 * For example:
 * Given binary tree [3,9,20,null,null,15,7],
 *    3
 *   / \
 *  9  20
 *  /  \
 * 15   7
 * return its zigzag level order traversal as:
 * [
 * [3],
 * [20,9],
 * [15,7]
 * ]
 * <p>
 * Created by drfish on 6/7/2017.
 */
public class _103BinaryTreeZigzagLevelOrderTraversal {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        List<TreeNode> curr = new ArrayList<>();
        boolean isOdd = true;

        if (root == null) {
            return result;
        }
        curr.add(root);

        while (!curr.isEmpty()) {
            List<TreeNode> next = new ArrayList<>();
            List<Integer> level = new LinkedList<>();
            for (TreeNode node : curr) {
                if (node.left != null) {
                    next.add(node.left);
                }
                if (node.right != null) {
                    next.add(node.right);
                }
                if (isOdd) {
                    level.add(node.val);
                } else {
                    level.add(0, node.val);
                }
            }
            isOdd = !isOdd;
            result.add(level);
            curr = next;
        }
        return result;
    }
}
