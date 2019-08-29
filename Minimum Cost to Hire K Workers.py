import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        breakpoint()
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, qsum * r)
        return res

quality = [10,20,5]
wage = [70,50,30]
K = 2
quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
K = 3
s = Solution()
print(s.mincostToHireWorkers(quality, wage, K))
