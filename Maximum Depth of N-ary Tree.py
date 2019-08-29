import queue
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = queue.Queue()
        q.put((root, 1))
        while not q.empty():
            node, current_count = q.get()
            count = current_count + 1
            max_count = max(max_count, current_count)
            for n in node.children:
                q.put((n, count))
        return count


