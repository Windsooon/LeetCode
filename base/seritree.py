class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class So:
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
                    if data[current_index] != None:
                        l.left = TreeNode(data[current_index])
                        tem.append(l.left)
                current_index += 1
                if current_index < len(data):
                    if data[current_index] != None:
                        l.right = TreeNode(data[current_index])
                        tem.append(l.right)
            level = tem
        return root
