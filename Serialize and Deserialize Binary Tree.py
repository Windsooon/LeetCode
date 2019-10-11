# Definition for a binary tree node.
import queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return
        import queue
        ans = [root.val]
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            top = q.get()
            if top:
                for child in [top.left, top.right]:
                    if child:
                        ans.append(child.val)
                        q.put(child)
                    else:
                        ans.append(None)
        return ans
     
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        count = 0
        root = TreeNode(data[count])
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            top = q.get()
            count += 1
            if data[count]:
                top.left = TreeNode(data[count])
                q.put(top.left)
            else:
                top.left = None
            count += 1
            if data[count]:
                top.right = TreeNode(data[count])
                q.put(top.right)
            else:
                top.right = None

        return root

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e
# Your Codec object will be instantiated and called as such:
codec = Codec()
res = codec.serialize(a)
codec.deserialize(res)
