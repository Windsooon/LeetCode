# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # '1-2-3--4'
        # We count how many dash for the current number
        # 0 -> '1', 1 -> '2'
        dash_count = 0
        # We use a dic to store the node for every level
        dic = {}
        current_val = ''
        i = 0
        while i < len(S):
            # string handle
            if S[i] == '-':
                dash_count += 1
                i += 1
                continue
            while i < len(S) and S[i] != '-':
                current_val += S[i]
                i += 1
            # Set up the root node
            if not dash_count:
                root = TreeNode(int(current_val))
                dic[0] = root
            else:
                # If the 'parent' already has left child
                # we set the current node to right child
                node = TreeNode(int(current_val))
                if dic[dash_count-1].left:
                    dic[dash_count-1].right = node
                else:
                    dic[dash_count-1].left = node
                # Set the current level
                dic[dash_count] = node
            dash_count = 0
            current_val = ''
        return root

s = Solution()
root = s.recoverFromPreorder("1-2--3--4-5--6--7")
