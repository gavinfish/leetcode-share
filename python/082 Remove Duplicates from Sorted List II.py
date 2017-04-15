'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def my_print(self):
        print(self.val)
        if self.next:
            print(self.next.val)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        is_repeat = False
        while curr.next:
            while curr.next.next and curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
                is_repeat = True
            if is_repeat:
                curr.next = curr.next.next
                is_repeat = False
            else:
                curr = curr.next
        return dummy.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n1.next = n2
    n2.next = n3
    r = Solution().deleteDuplicates(n1)
    r.my_print()