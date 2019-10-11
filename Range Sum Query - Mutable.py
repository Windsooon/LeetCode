class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class NumArray:

    def __init__(self, nums):
        self.lst = nums
        self.root = self.build_tree(0, len(self.lst)-1, self.lst)
        
    def build_tree(self, left, right, lst):
        if not lst:
            return
        if left == right:
            return TreeNode(lst[left])
        root = TreeNode(1)
        mid = (left+right)//2
        left_tree = self.build_tree(left, mid, lst)
        right_tree = self.build_tree(mid+1, right, lst)
        root.val = left_tree.val + right_tree.val
        root.left = left_tree
        root.right = right_tree
        return root

    def update(self, i: int, val: int) -> None:
        diff = val - self.lst[i]
        self.lst[i] = val
        self.update_tree(diff, i, 0, len(self.lst)-1, self.root)
    
    def update_tree(self, diff, index, left, right, node):
        node.val += diff
        if left < right:
            mid = (left + right) // 2
            if index <= mid:
                self.update_tree(diff, index, left, mid, node.left)
            else:
                self.update_tree(diff, index, mid+1, right, node.right)

    def sumRange(self, i: int, j: int) -> int:
        return self.query_tree(i, j, self.root, 0, len(self.lst)-1)

    def query_tree(self, start, end, node, node_start, node_end):
        # base case
        if start == end:
            return self.lst[start]
        elif start == node_start and end == node_end:
            return node.val
        mid = (start + end) // 2
        if end <= mid:
            return self.query_tree(start, end, node.left, node_start, (node_start+node_end)//2)
        elif start > mid:
            return self.query_tree(start, end, node.right, (node_start+node_end)//2+1, node_end)
        else:
            return self.query_tree(start, mid, node.left, node_start, (node_start+node_end)//2) + self.query_tree(mid+1, end, node.right, (node_start+node_end)//2+1, node_end)

def levelorder(node):
    level = [node]
    while level:
        tem = []
        for l in level:
            print(l.val)
            for child in [l.left, l.right]:
                if child:
                    tem.append(child)
        level = tem

s = NumArray([7,2,7,2,0])
s.update(4, 6)
s.update(0, 2)
s.update(0, 9)
s.sumRange(4, 4)
s.update(3, 8)
s.sumRange(0, 4)
s.update(4, 1)
print(s.sumRange(0, 3))
# levelorder(s.root)
# ["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"]
# [[[7,2,7,2,0]],[4,6],[0,2],[0,9],       [4,4],     [3,8],    [0,4],    [4,1],    [0,3],[0,4],[0,4]]
