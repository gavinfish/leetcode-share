'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''

class LRUCache(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev, self.next = None, None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity, self.size = capacity, 0
        self.dic = {}
        self.head, self.tail = self.Node(-1, -1), self.Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def __remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def __insert(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.__remove(node)
        self.__insert(node)
        return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            node = self.dic[key]
            self.__remove(node)
            node.value = value
            self.__insert(node)
        else:
            if self.size == self.capacity:
                discard = self.tail.prev
                self.__remove(discard)
                del self.dic[discard.key]
                self.size -= 1
            node = self.Node(key, value)
            self.dic[key] = node
            self.__insert(node)
            self.size += 1


if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)
    assert lru_cache.get(0) == -1
    assert lru_cache.get(1) == 1
    lru_cache.set(1, 10)
    assert lru_cache.get(1) == 10
    lru_cache.set(4, 4)
    assert lru_cache.get(2) == -1