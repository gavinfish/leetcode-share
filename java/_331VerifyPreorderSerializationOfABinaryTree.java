import java.util.Stack;

/**
 * One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
 * <p>
 *      _9_
 *     /   \
 *    3     2
 *   / \   / \
 *  4   1  #  6
 * / \ / \   / \
 * # # # #   # #
 * For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
 * Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.
 * Each comma separated value in the string must be either an integer or a character '#' representing null pointer.
 * You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".
 * <p>
 * Example 1:
 * "9,3,4,#,#,1,#,#,2,#,6,#,#"
 * Return true
 * <p>
 * Example 2:
 * "1,#"
 * Return false
 * <p>
 * Example 3:
 * "9,#,#,1"
 * Return false
 * <p>
 * Credits:
 * Special thanks to @dietpepsi for adding this problem and creating all test cases.
 * <p>
 * Created by drfish on 6/9/2017.
 */
public class _331VerifyPreorderSerializationOfABinaryTree {
    public boolean isValidSerialization(String preorder) {
        Stack<String> stack = new Stack<>();
        String[] splits = preorder.split(",");
        for (String s : splits) {
            while (s.equals("#") && !stack.isEmpty() && stack.peek().equals("#")) {
                stack.pop();
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
            stack.push(s);
        }
        return stack.size() == 1 && stack.peek().equals("#");
    }

    public static void main(String[] args) {
        _331VerifyPreorderSerializationOfABinaryTree solution = new _331VerifyPreorderSerializationOfABinaryTree();
        assert solution.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#");
        assert !solution.isValidSerialization("1,#");
        assert !solution.isValidSerialization("9,#,#,1");
    }
}
