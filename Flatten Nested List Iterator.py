from collections import deque


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = deque()
        self.queue.extend(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.queue:
            return False
        if isinstance(self.queue[0], int):
            return True
        else:
            left = self.queue.popleft()
            if left:
                self.queue.extendleft(left[::-1])
                return True
            else:
                return self.hasNext()

n = NestedIterator([[]])
while n.hasNext():
    print((n.next()))
