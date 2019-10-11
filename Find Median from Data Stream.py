import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.small, self.big = [], []
        heapq.heapify(self.small)
        heapq.heapify(self.big)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.big, num)
        if len(self.small) < len(self.big):
            top = heapq.heappop(self.big)
            heapq.heappush(self.small, -top)
        
    def findMedian(self) -> float:
        breakpoint()
        if len(self.small) > len(self.big):
            return -self.small[0]
        else:
            return (-self.small[0] + self.big[0]) / 2

m = MedianFinder()
m.addNum(1)
m.addNum(2)
print(m.findMedian())
