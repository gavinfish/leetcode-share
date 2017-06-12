import java.util.PriorityQueue;

/**
 * Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
 * not the kth distinct element.
 * <p>
 * For example,
 * Given [3,2,1,5,6,4] and k = 2, return 5.
 * <p>
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ array's length.
 * <p>
 * Credits:
 * Special thanks to @mithmatt for adding this problem and creating all test cases.
 * <p>
 * Created by drfish on 10/06/2017.
 */
public class _215KthLargestElementInAnArray {
    /**
     * heap solution
     */
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int num : nums) {
            heap.offer(num);
            if (heap.size() > k) {
                heap.poll();
            }
        }
        return heap.peek();
    }

    public static void main(String[] args) {
        _215KthLargestElementInAnArray solution = new _215KthLargestElementInAnArray();
        assert 5 == solution.findKthLargest(new int[]{3, 2, 1, 5, 6, 4}, 2);
    }
}
