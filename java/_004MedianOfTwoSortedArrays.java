import com.sun.org.apache.regexp.internal.recompile;

/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 * <p>
 * Example 1:
 * nums1 = [1, 3]
 * nums2 = [2]
 * The median is 2.0
 * <p>
 * Example 2:
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * The median is (2 + 3)/2 = 2.5
 * <p>
 * Created by drfish on 04/05/2017.
 */
public class _004MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int k1 = (nums1.length + nums2.length + 1) / 2;
        int k2 = (nums1.length + nums2.length + 2) / 2;
        return (findK(nums1, 0, nums2, 0, k1) + findK(nums1, 0, nums2, 0, k2)) / 2.0;
    }

    private double findK(int[] nums1, int start1, int[] nums2, int start2, int k) {
        if (start1 >= nums1.length) {
            return nums2[start2 + k - 1];
        }
        if (start2 >= nums2.length) {
            return nums1[start1 + k - 1];
        }
        if (k == 1) {
            return Math.min(nums1[start1], nums2[start2]);
        }
        int mid1 = Integer.MAX_VALUE;
        int mid2 = Integer.MAX_VALUE;
        if (start1 + k / 2 - 1 < nums1.length) {
            mid1 = nums1[start1 + k / 2 - 1];
        }
        if (start2 + k / 2 - 1 < nums2.length) {
            mid2 = nums2[start2 + k / 2 - 1];
        }
        if (mid1 < mid2) {
            return findK(nums1, start1 + k / 2, nums2, start2, k - k / 2);
        } else {
            return findK(nums1, start1, nums2, start2 + k / 2, k - k / 2);
        }
    }
}
