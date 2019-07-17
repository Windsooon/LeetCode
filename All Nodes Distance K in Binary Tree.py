import collections
import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.table = collections.defaultdict(list)
        self.inorder(root, None)
        return self.bfs_f(target, 0, K)

    def inorder(self, node, parent):
        '''
        Create a dic from graph (it's root node is node)
        Add element to self.table, the key is node, and the value
        is the list of parent and childs
        >>> inorder(5)
        >>> self.table[5]
        >>> [3, 6, 2]
        '''
        if not node:
            return
        if parent:
            self.table[node.val].append(parent.val)
        if node.left:
            self.table[node.val].append(node.left.val)
        if node.right:
            self.table[node.val].append(node.right.val)
        self.inorder(node.left, node)
        self.inorder(node.right, node)

    def bfs_f(self, node, level, K):
        bfs = [node]
        seen = set(bfs)
        for i in range(K):
            bfs = [y for x in bfs for y in self.table[x] if y not in seen]
            seen |= set(bfs)
        return bfs



a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
a.left = b
a.right = c

d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(0)

g = TreeNode(8)
h = TreeNode(7)
i = TreeNode(4)

b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i

target = 5
K = 0

s = Solution()
print(s.distanceK(a, target, K))
