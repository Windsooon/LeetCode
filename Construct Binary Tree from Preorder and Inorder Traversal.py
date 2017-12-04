class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if inorder:
            root = preorder.pop(0)
            print(root)
            index = inorder.index(root)
            node = TreeNode(root)
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            return node

pre = [1, 5, 15, 23, 8, 7, 12]
inorder = [15, 5, 23, 1, 7, 8, 12]

s = Solution()
s.buildTree(pre, inorder)
