/**
 * Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
 * <p>
 * For example,
 * Given n = 3, there are a total of 5 unique BST's.
 * <p>
 * 1         3     3      2      1
 *  \       /     /      / \      \
 *   3     2     1      1   3      2
 *  /     /       \                 \
 * 2     1         2                 3
 * <p>
 * Created by drfish on 27/05/2017.
 */
public class _096UniqueBinarySearchTrees {
    public int numTrees(int n) {
        int[] counts = new int[n + 1];
        counts[0] = 1;
        for (int i = 1; i <= n; i++) {
            int count = 0;
            for (int j = 0; j < i; j++) {
                count += counts[j] * counts[i - 1 - j];
            }
            counts[i] = count;
        }
        return counts[n];
    }

    public static void main(String[] args) {
        _096UniqueBinarySearchTrees uniqueBinarySearchTrees = new _096UniqueBinarySearchTrees();
        assert uniqueBinarySearchTrees.numTrees(3) == 5;
        assert uniqueBinarySearchTrees.numTrees(6) == 132;
    }
}
