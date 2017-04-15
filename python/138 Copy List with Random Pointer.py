'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        visited = dict()
        node = head
        while node:
            visited[node] = RandomListNode(node.label)
            node = node.next

        visited[None] = None
        node = head
        while node:
            visited[node].next = visited[node.next]
            visited[node].random = visited[node.random]
            node = node.next
        return visited[head]


if __name__ == "__main__":
    None