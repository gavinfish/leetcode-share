import java.util.Arrays;

/**
 * Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the
 * very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
 * <p>
 * For example,
 * Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
 * <p>
 * Window position                Max
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 *  1 [3  -1  -3] 5  3  6  7       3
 *  1  3 [-1  -3  5] 3  6  7       5
 *  1  3  -1 [-3  5  3] 6  7       5
 *  1  3  -1  -3 [5  3  6] 7       6
 *  1  3  -1  -3  5 [3  6  7]      7
 * Therefore, return the max sliding window as [3,3,5,5,6,7].
 * <p>
 * Note:
 * You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
 * <p>
 * Follow up:
 * Could you solve it in linear time?
 * <p>
 * Created by drfish on 12/06/2017.
 */
public class _239SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length < 1) {
            return new int[0];
        }
        int[] leftMax = new int[nums.length];
        int[] rightMax = new int[nums.length];
        leftMax[0] = nums[0];
        rightMax[nums.length - 1] = nums[nums.length - 1];
        for (int i = 1; i < nums.length; i++) {
            leftMax[i] = (i % k == 0) ? nums[i] : Math.max(leftMax[i - 1], nums[i]);
            int j = nums.length - i - 1;
            rightMax[j] = (j % k == 0) ? nums[j] : Math.max(rightMax[j + 1], nums[j]);
        }
        int[] result = new int[nums.length - k + 1];
        for (int i = 0; i + k <= nums.length; i++) {
            result[i] = Math.max(leftMax[i + k - 1], rightMax[i]);
        }
        return result;
    }

    public static void main(String[] args) {
        _239SlidingWindowMaximum solution = new _239SlidingWindowMaximum();
        assert Arrays.equals(new int[]{3, 3, 5, 5, 6, 7}, solution.maxSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6,
                7}, 3));
    }
}
