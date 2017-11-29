import java.util.List;

import javax.management.relation.RelationTypeSupport;
import javax.swing.tree.TreeNode;

/**
 * Given a binary tree, return all root-to-leaf paths.
 * 
 * For example, given the following binary tree:
 * 
 *    1
 *  /   \
 * 2     3
 *  \
 *   5
 * All root-to-leaf paths are:
 * 
 * ["1->2->5", "1->3"]
 */

public class _257BinaryTreePaths {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        if (root != null) {
            search(root, "", result);
        }
        return result;
    }

    public void search(TreeNode node, String path, List<String> result) {
        if (node.left == null && node.right == null) {
            result.add(path + node.val);
        }
        if (node.left != null) {
            search(node.left, path + node.val + "->", result);
        }
        if (node.right != null) {
            search(node.right, path + node.val + "->", result);
        }
    }
}