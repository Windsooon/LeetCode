class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        lst = [1, 1]
        for i in range(2, n+1):
            results = 0
            for j in range(i):
                results += lst[j] * lst[i-j-1]
            lst.append(results)
        return lst[n]

s = Solution()
print(s.numTrees(3))
