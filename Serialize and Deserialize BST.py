# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(root):
            if not root:
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(res)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst  = collections.deque(data.split(','))
        def decode(min_val, max_val):
            if not lst:
                return
            if min_val < int(lst[0]) < max_val:
                root = TreeNode(int(lst.popleft()))
                root.left = decode(min_val, root.val)
                root.right = decode(root.val, max_val)
                return root
        return decode(float('-inf'), float('inf'))

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
b.left = a
b.right = c
codec = Codec()
codec.deserialize(codec.serialize(b))
