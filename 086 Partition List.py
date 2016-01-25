'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        small_dummy = ListNode(-1)
        large_dummy = ListNode(-1)

        prev = dummy
        small_prev = small_dummy
        large_prev = large_dummy
        while prev.next:
            curr = prev.next
            if curr.val < x:
                small_prev.next = curr
                small_prev = small_prev.next
            else:
                large_prev.next = curr
                large_prev = large_prev.next
            prev = prev.next
        large_prev.next = None
        small_prev.next = large_dummy.next
        return small_dummy.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(5)
    n6 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    r = Solution().partition(n1, 3)
    assert r.to_list() == [1, 2, 2, 4, 3, 5]