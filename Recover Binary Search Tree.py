# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if not root:
            return
        # a list to store node to be exchange
        change = []
        lst = self.inorder(root)
        for i in range(len(lst)-1):
            if lst[i+1].val < lst[i].val:
                # If we already found the first one i, the seconde one would be i+1
                # you can find that in the second example given by Leetcode
                if change:
                    change.append(i+1)
                else:
                    change.append(i)
        # exchange elements
        if len(change) == 1:
            lst[change[0]].val, lst[change[0]+1].val = lst[change[0]+1].val, lst[change[0]].val
        else:
            lst[change[0]].val, lst[change[1]].val = lst[change[1]].val, lst[change[0]].val


    def inorder(self, root):
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            top = stack.pop()
            res.append(top)
            root = top.right
        return res


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)
d = TreeNode(2)
a.left = b
a.right = c
c.left = d


s = Solution()
print(s.recoverTree(a))
