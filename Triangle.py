class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ans = 0
        start = 0
        end = 1
        for t in triangle:
            min_element = min(t[start:end+1])
            ans += min_element
            new = t.index(min_element)
            start = new
            end = new + 1
        return ans

tri = [[-1],[2,3],[1,-1,-3]]
s = Solution()
print(s.minimumTotal(tri))
