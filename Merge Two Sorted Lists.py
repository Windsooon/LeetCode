import heapq


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
        an, h = [], []
        for k in lists:
            while k:
                heapq.heappush(h, k.val)
                k = k.next
        while h:
            an.append(heapq.heappop(h))
        return an

c = Solution()
k = []
f = ListNode(1)
k.append(f)
print(c.mergeKLists(k))
