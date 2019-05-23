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
        res = []
        if not root:
            return []
        # [[1, False]]
        stack = [[root, False]]
        while stack:
            top = stack.pop()
            if top[1]:
                res.append(top[0].val)
            else:
                stack.append([top[0], True])
                if top[0].right:
                    stack.append([top[0].right, False])
                if top[0].left:
                    stack.append([top[0].left, False])
        return res


root = TreeNode(1)
root.left = None
root.right = TreeNode(3)

c = Solution()
print(c.postorderTraversal(root))
