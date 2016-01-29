'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        return [self.val] + self.next.to_list() if self.next else [self.val]


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev = head
        curr = prev.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head.next = None
        return prev


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    r = Solution().reverseList(n1)
    assert r.to_list() == [3, 2, 1]