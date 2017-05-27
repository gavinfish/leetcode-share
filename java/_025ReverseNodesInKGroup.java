/**
 * Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
 * <p>
 * k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
 * <p>
 * You may not alter the values in the nodes, only nodes itself may be changed.
 * <p>
 * Only constant memory is allowed.
 * <p>
 * For example,
 * Given this linked list: 1->2->3->4->5
 * <p>
 * For k = 2, you should return: 2->1->4->3->5
 * <p>
 * For k = 3, you should return: 3->2->1->4->5
 * <p>
 * Created by drfish on 16/04/2017.
 */
public class _025ReverseNodesInKGroup {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k <= 1)
            return head;
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        for (ListNode prev = dummy, end = head; end != null; end = prev.next) {
            for (int i = 1; i < k && end != null; i++)
                end = end.next;
            if (end == null)
                break;
            prev = reverse(prev, prev.next, end);
        }
        return dummy.next;
    }

    private ListNode reverse(ListNode prev, ListNode start, ListNode end) {
        ListNode endNext = end.next;
        for (ListNode p = start, cur = p.next, next = cur.next;
             cur != endNext;
             p = cur, cur = next, next = next != null ? next.next : null)
            cur.next = p;
        start.next = endNext;
        prev.next = end;
        return start;
    }
}
