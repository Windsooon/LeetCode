import heapq
import bisect

class Solution:
    def oddEvenJumps(self, A):
        if len(A) == 1:
            return 1
        count = 1
        dp = [[False]*2 for i in range(len(A))]
        dp[-1][0] = True
        dp[-1][1] = True
        lst = [(A[-1], len(A)-1)]
        breakpoint()
        for i in range(len(A)-2, -1, -1):
            lst.sort()
            k = bisect.bisect_right(lst, (A[i], i))
            if k != len(A):
                count += dp[lst[k][1]][1]
                dp[i][0] = dp[lst[k][1]][1]
            j = bisect.bisect_left(lst, (A[i], i))
            if j != 0:
                dp[i][1] = dp[lst[j][1]][0]
            lst.append((A[i], i))
        return count



s = Solution()
print(s.oddEvenJumps([2,3,1,1,4]))
# print(s.oddEvenJumps([10,13,12,14,15]))
