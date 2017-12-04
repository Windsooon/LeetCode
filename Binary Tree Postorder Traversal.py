class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        first, second = [], []
        first.append(root)
        while first:
            last = first.pop()
            second.append(last.val)
            if last.left:
                first.append(last.left)
            if last.right:
                first.append(last.right)
        return second[::-1]

root = TreeNode(1)
root.left = None
root.right = TreeNode(2)

c = Solution()
print(c.postorderTraversal(root))
