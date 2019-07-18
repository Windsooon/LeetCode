from statistics import mean
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def averageOfLevels(self, root):
        return list(map(mean, self.levelOrder(root)))

    # copied&pasted from old problem's solution:
    def levelOrder(self, root):
        levels = []
        level = [root]
        while any(level):
            levels.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return levels
