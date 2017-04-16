/**
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * <p>
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * <p>
 * Created by drfish on 16/04/2017.
 */

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

public class _002AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode cur = result;
        while (l1 != null || l2 != null) {
            cur.val += addTwoNodes(l1, l2);
            if (cur.val >= 10) {
                cur.val -= 10;
                cur.next = new ListNode(1);
            } else {
                if (l1 != null && l1.next != null || l2 != null && l2.next != null)
                    cur.next = new ListNode(0);
            }
            cur = cur.next;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }
        return result;
    }

    private int addTwoNodes(ListNode n1, ListNode n2) {
        if (n1 == null)
            return n2.val;
        if (n2 == null)
            return n1.val;
        return n1.val + n2.val;
    }
}
