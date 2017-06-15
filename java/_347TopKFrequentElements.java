import java.util.*;

/**
 * Given a non-empty array of integers, return the k most frequent elements.
 * <p>
 * For example,
 * Given [1,1,1,2,2,3] and k = 2, return [1,2].
 * <p>
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 * Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 * <p>
 * Created by drfish on 15/06/2017.
 */
public class _347TopKFrequentElements {
    public List<Integer> topKFrequent(int[] nums, int k) {
        List<Integer> result = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap = new PriorityQueue<>((n1, n2) -> n2.getValue() -
                n1.getValue());
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            maxHeap.offer(entry);
        }
        while (k > 0) {
            k--;
            result.add(maxHeap.poll().getKey());
        }
        return result;
    }

    public static void main(String[] args) {
        _347TopKFrequentElements solution = new _347TopKFrequentElements();
        assert Arrays.asList(1, 2).equals(solution.topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2));
    }
}
