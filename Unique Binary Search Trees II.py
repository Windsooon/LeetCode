# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        breakpoint()
        return self.rec(list(range(1, n+1)))

    def rec(self, lst):
        if not lst:
            return [None]
        ans = []
        for k in range(len(lst)):
            for left in self.rec(lst[:k]):
                for right in self.rec(lst[k+1:]):
                    root = TreeNode(lst[k])
                    root.left = left
                    root.right = right
                    ans.append(root)
        return ans

n = 3
s = Solution()
s.generateTrees(n)
