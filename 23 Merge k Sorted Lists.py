'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        temp = ListNode(-1)
        head = temp
        while heap:
            smallestNode = heapq.heappop(heap)[1]
            temp.next = smallestNode
            temp = temp.next
            if smallestNode.next:
                heapq.heappush(heap, (smallestNode.next.val, smallestNode.next))
        return head.next