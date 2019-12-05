class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        return self.binary_search(K+1) - self.binary_search(K)

    def find_zeros(self, num):
        res = 0
        while num:
            res += num // 5
            num = num // 5
        return res

    def binary_search(self, K):
        left, right = 0, 5 * K + 1
        while left < right:
            mid = (left + right) // 2
            cal = self.find_zeros(mid)
            if cal < K:
                left = mid + 1
            else:
                right = mid
        return left

s = Solution()
print(s.preimageSizeFZF(0))
