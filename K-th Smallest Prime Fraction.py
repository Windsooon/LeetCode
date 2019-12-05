import heapq

class Solution:
    def kthSmallestPrimeFraction(self, A, K: int):
        h = []
        for i in range(len(A)-1):
            heapq.heappush(h, (A[i]/A[-1], i, len(A)-1))
        while K > 0:
            K -= 1
            num, start, end = heapq.heappop(h)
            if K == 0: 
                return [A[start], A[end]]
            else:
                if end - start > 1:
                    heapq.heappush(h, (A[start]/A[end-1], start, end-1))


s = Solution()
breakpoint()
s.kthSmallestPrimeFraction([1,2,3,5], 3)
