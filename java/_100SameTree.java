/**
 * Given two binary trees, write a function to check if they are equal or not.
 * Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
 * <p>
 * Created by drfish on 28/05/2017.
 */
public class _100SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p != null && q != null) {
            if (p.val == q.val) {
                return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
            }
        }
        return false;
    }
}
