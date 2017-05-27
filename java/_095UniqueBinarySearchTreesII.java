import java.util.ArrayList;
import java.util.List;

/**
 * Created by drfish on 27/05/2017.
 */
public class _095UniqueBinarySearchTreesII {
    public List<TreeNode> generateTrees(int n) {
        List<TreeNode> result = genTrees(1, n);
        if (result.get(0) == null) {
            return new ArrayList<>();
        } else {
            return result;
        }
    }

    private List<TreeNode> genTrees(int start, int end) {
        List<TreeNode> result = new ArrayList<>();
        if (start > end) {
            result.add(null);
        }
        for (int i = start; i <= end; i++) {
            List<TreeNode> leftTrees = genTrees(start, i - 1);
            List<TreeNode> rightTrees = genTrees(i + 1, end);
            for (TreeNode leftTree : leftTrees) {
                for (TreeNode rightTree : rightTrees) {
                    TreeNode root = new TreeNode(i);
                    root.left = leftTree;
                    root.right = rightTree;
                    result.add(root);
                }
            }
        }
        return result;
    }
}
