    class Solution:
        def smallestRange(self, A):
            import heapq
            # create a heap for first element of each list, for example [0, 4, 5]
            lst = [(l[0], i, 0) for i, l in enumerate(A)]
            heapq.heapify(lst)
    
            left = min(l[0] for l in A)
            right = max(l[0] for l in A)
            # first answer will be [0, 5]
            ans = [left, right]
            while lst:
                left, a, b = heapq.heappop(lst)
                # check smallest range
                if (right - left) < (ans[1] - ans[0]) or \
                        ((right - left) == (ans[1] - ans[0]) and left < ans[0]):
                    ans = [left, right]
                if b + 1 == len(A[a]):
                    return ans
                # make sure the heaq will keep one element from each list
                heapq.heappush(lst, (A[a][b+1], a, b+1))
                if A[a][b+1] > right:
                    right = A[a][b+1]
