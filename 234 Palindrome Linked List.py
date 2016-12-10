'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # split the list into two parts, we can reverse the first part at meantime
        fast = slow = head
        reverse = None
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        # if the total number is odd, skip the centre point
        if fast:
            slow = slow.next
        # compare the reversed first part and normal second part
        while reverse:
            if reverse.val != slow.val:
                return False
            else:
                reverse = reverse.next
                slow = slow.next
        return True


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n1.next = n2
    n2.next = n3
    assert Solution().isPalindrome(n1) == True
    assert Solution().isPalindrome(n2) == False
    n1.next = n3
    assert Solution().isPalindrome(n1) == True
