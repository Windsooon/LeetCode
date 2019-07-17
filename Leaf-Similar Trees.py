# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        lst1, lst2 = [], []
        self.inorder_lst(root1, lst1)
        self.inorder_lst(root2, lst2)
        return lst1 == lst2
    
    def inorder_lst(self, root, lst):
        if not root:
            return
        self.inorder_lst(root.left, lst)
        if not root.left and not root.right:
            lst.append(root.val)
        self.inorder_lst(root.right, lst)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

d = TreeNode(1)
e = TreeNode(2)
f = TreeNode(3)
d.left = e
d.right = f

s = Solution()
print(s.leafSimilar(a, d))
