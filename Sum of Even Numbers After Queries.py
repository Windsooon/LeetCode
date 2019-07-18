class Solution:
    def sumEvenAfterQueries(self, A, queries):
        # [1, 2, 3, 4] -> 6
        base = sum(i for i in A if i % 2 == 0)
        ans = []
        for q in queries:
            target = A[q[1]]
            changed = q[0] + target
            if target % 2 == 0:
                if changed % 2 == 0:
                    base = base - target + changed
                else:
                    base = base - target
            else:
                if changed % 2 == 0:
                    base = base + changed
            ans.append(base)
            A[q[1]] = changed
        return ans


s = Solution()
A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(s.sumEvenAfterQueries(A, queries))
