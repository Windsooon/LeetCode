def isBadVersion(version):
    a = [False, True]
    return a[version-1]


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while right - left > 1:
            mid = left + (right-left)//2
            current_version = isBadVersion(mid)
            if current_version:

            else:
                left = mid
        return 1


s = Solution()
print(s.firstBadVersion(2))
