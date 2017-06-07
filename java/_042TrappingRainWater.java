import java.util.Stack;

/**
 * Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
 * <p>
 * For example,
 * Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
 * <p>
 * The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
 * <p>
 * Created by drfish on 6/7/2017.
 */
public class _042TrappingRainWater {
    public int trap(int[] height) {
        if (height == null) {
            return 0;
        }
        int leftIndex = 0;
        int rightIndex = height.length - 1;
        int leftMax = 0;
        int rightMax = 0;
        int result = 0;

        while (leftIndex <= rightIndex) {
            if (height[leftIndex] <= height[rightIndex]) {
                if (height[leftIndex] >= leftMax) {
                    leftMax = height[leftIndex];
                } else {
                    result += leftMax - height[leftIndex];
                }
                leftIndex++;
            } else {
                if (height[rightIndex] >= rightMax) {
                    rightMax = height[rightIndex];
                } else {
                    result += rightMax - height[rightIndex];
                }
                rightIndex--;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        _042TrappingRainWater solution = new _042TrappingRainWater();
        int[] height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        assert 6 == solution.trap(height);
        assert 0 == solution.trap(new int[]{0, 2, 0});
    }
}
