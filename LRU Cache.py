class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        pass

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        pass

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        pass


lru = LRUCache(2)
lru.put(2, 1)
lru.put(1, 1)
lru.put(2, 3)
lru.put(4, 1)
lru.get(1)
lru.get(2)
