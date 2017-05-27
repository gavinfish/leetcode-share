import java.util.PriorityQueue;

/**
 * Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
 * <p>
 * Created by drfish on 16/04/2017.
 */
public class _023MergeKSortedLists {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> nodesHeap = new PriorityQueue<ListNode>((n1, n2) -> (n1.val - n2.val));
        for (ListNode node : lists) {
            if (node != null)
                nodesHeap.add(node);
        }
        ListNode dummy = new ListNode(-1);
        ListNode head = dummy;
        while (!nodesHeap.isEmpty()) {
            ListNode node = nodesHeap.poll();
            if (node.next != null)
                nodesHeap.add(node.next);
            dummy.next = node;
            dummy = dummy.next;
        }
        return head.next;
    }
}
