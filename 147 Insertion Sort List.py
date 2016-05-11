'''
Sort a linked list using insertion sort.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        while head:
            # check if it is needed to reset the cur pointer
            if cur and cur.val > head.val:
                cur = dummy
            # find the place to insert
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            # insert and sort the next element
            cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next


if __name__ == "__main__":
    None