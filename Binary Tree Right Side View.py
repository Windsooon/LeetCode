# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append(level[-1].val)
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans

a = TreeNode(5)
a.left = TreeNode(5)
a.right = TreeNode(5)
a.right.right = TreeNode(5)
a.right.right.left = TreeNode(5)
a.left.left = TreeNode(5)
a.left.right = TreeNode(1)

s = Solution()
print(s.rightSideView(a))
