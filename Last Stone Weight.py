import queue

class Solution:
    def lastStoneWeight(self, stones):
        q = queue.PriorityQueue()
        for s in stones:
            # -8, -7, -4, -2, -1, -1
            q.put(-s)

        for i in range(len(stones)-1):
            biggest = q.get()
            second = q.get()
            q.put(-((-biggest)-(-second)))
        return -q.get()

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
