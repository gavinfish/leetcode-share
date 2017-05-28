/**
 * Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
 * <p>
 * For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
 *     1
 *    / \
 *   2   2
 *  / \ / \
 * 3  4 4  3
 * But the following [1,2,2,null,3,null,3] is not:
 *   1
 *  / \
 * 2   2
 *  \   \
 *  3    3
 * <p>
 * Note:
 * Bonus points if you could solve it both recursively and iteratively.
 * <p>
 * Created by drfish on 28/05/2017.
 */
public class _101SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return check(root.left, root.right);
    }

    private boolean check(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p != null && q != null) {
            if (p.val == q.val) {
                return check(p.left, q.right) && check(p.right, q.left);
            }
        }
        return false;
    }
}
