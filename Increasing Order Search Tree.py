# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        if not root:
            return
        ans = []
        stack = []
        visited = set()
        while root:
            if (not root.left and not root.right) or root in visited:
                ans.append(root.val)
                if not stack:
                    break
                root = stack.pop()
                continue
            stack.append(root.left)
            stack.append(root)
            stack.append(root.right)
            visited.add(root)
            root = stack.pop()
        return ans[::-1]

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e


s = Solution()
node = s.inorderTraversal(a)
print(node)
