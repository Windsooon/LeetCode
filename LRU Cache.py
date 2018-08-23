import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            value = self.dic.pop(key)
            self.dic[key] = value
            print(self.dic[key])
            return self.dic[key]
        else:
            print(-1)
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self.dic.pop(key)
            self.dic[key] = value
            return
        if len(self.dic) >= self.capacity:
            self.dic.popitem(last=False)
        self.dic[key] = value


lru = LRUCache(2)
lru.put(2, 1)
lru.put(1, 1)
lru.put(2, 3)
lru.put(4, 1)
lru.get(1)
lru.get(2)
