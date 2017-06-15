import java.util.Stack;

/**
 * Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
 * <p>
 * Note: n will be less than 15,000.
 * <p>
 * Example 1:
 * Input: [1, 2, 3, 4]
 * Output: False
 * Explanation: There is no 132 pattern in the sequence.
 * <p>
 * Example 2:
 * Input: [3, 1, 4, 2]
 * Output: True
 * Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
 * <p>
 * Example 3:
 * Input: [-1, 3, 2, 0]
 * Output: True
 * Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 * <p>
 * Created by drfish on 6/13/2017.
 */
public class _456132Pattern {
    public boolean find132pattern(int[] nums) {
        int num3 = Integer.MIN_VALUE;
        Stack<Integer> stack = new Stack<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] < num3) {
                return true;
                // always track the largest third num
            } else while (!stack.isEmpty() && nums[i] > stack.peek()) {
                num3 = stack.pop();
            }
            stack.push(nums[i]);
        }
        return false;
    }

    public static void main(String[] args) {
        _456132Pattern solution = new _456132Pattern();
        assert !solution.find132pattern(new int[]{1, 2, 3, 4});
        assert solution.find132pattern(new int[]{3, 1, 4, 2});
        assert solution.find132pattern(new int[]{-1, 3, 2, 0});
    }
}
