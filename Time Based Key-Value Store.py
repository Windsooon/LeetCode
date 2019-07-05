import collections

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.lst = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.lst[key].append(timestamp)
        self.dic[timestamp] = value

    def get(self, key, timestamp):
        if key not in self.lst:
            return
        return self.get_val(self.lst[key], timestamp)

    def get_val(self, lst, timestamp):
        """
        Find the biggest element in lst that smaller than timestamp
        input:
            lst: contains valid value from key
            timestamp: target timestamp
        """
        # find the correct index to insert timestamp in lst
        left = 0
        val = float('-inf')
        right = len(lst)
        while left < right:
            mid = (right+left)//2
            if lst[mid] <= timestamp:
                left = mid + 1
            else:
                right = mid
        if left - 1 < 0:
            return ''
        return self.dic[lst[left-1]]

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
# obj.set('foo','bar',1)
# print(obj.get('foo', 1))
# print(obj.get('foo', 3))
# obj.set('foo','bar2',4)
# print(obj.get('foo', 4))
# print(obj.get('foo', 5))
obj.set('love','high',10)
obj.set('love','low',20)
print(obj.get('love', 5))
print(obj.get('love', 10))
print(obj.get('love', 15))
print(obj.get('love', 20))
print(obj.get('love', 25))
