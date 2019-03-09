class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # import pdb; pdb.set_trace()
        # [73, 74, 75, 71, 69, 72, 76, 73]
        if not T:
            return []
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                top = stack.pop()
                ans[top] = i-top
            stack.append(i)
        return ans


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
