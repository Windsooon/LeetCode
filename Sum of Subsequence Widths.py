class Solution:
    def sumSubseqWidths(self, A):
        ans = 0
        A = sorted(A)
        total = 2**(len(A))
        for i in range(len(A)):
            ans += A[i] << i
            ans -= A[i] << (len(A)-i-1)
            ans = ans % (10**9 + 7)
        return ans

s = Solution()
print(s.sumSubseqWidths([5,69,89,92,31,16,25,45,63,40,16,56,24,40,75,82,40,12,50,62,92,44,67,38,92,22,91,24,26,21,100,42,23,56,64,43,95,76,84,79,89,4,16,94,16,77,92,9,30,13]))
