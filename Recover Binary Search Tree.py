class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lst = self.inorder(root)
        # 3 -> 2 -> 1
        

    def inorder(self, root):
        if not root:
            return
        lst = []
        stack = []
        while root or stack:
            if not root:
                root = stack.pop()
                lst.append(root)
                root = root.right
            else:
                stack.append(root)
                root = root.left
        return lst

