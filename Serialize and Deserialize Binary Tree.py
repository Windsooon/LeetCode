class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # breakpoint()
        if not root:
            return []
        res = [root.val]
        level = [root]
        while level:
            tem = []
            for l in level:
                if l:
                    for child in [l.left, l.right]:
                        tem.append(child)
            res.extend(i.val if i else None for i in tem)
            level = tem
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # breakpoint()
        if not data:
            return
        root = TreeNode(data[0])
        level = [root]
        current_index = 0
        while level and current_index < len(data):
            tem = []
            for l in level:
                current_index += 1
                if current_index < len(data):
                    l.left = TreeNode(data[current_index])
                    tem.append(l.left)
                current_index += 1
                if current_index < len(data):
                    l.right = TreeNode(data[current_index])
                    tem.append(l.right)
            level = tem
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
root = codec.deserialize(res)
breakpoint()
print(100)
