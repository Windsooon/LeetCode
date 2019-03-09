class Node:
    def __init__(self, val):
        self.val = val

    @property
    def left(self):
        self.left = self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        self.right = self._right

    @right.setter
    def right(self, node):
        self._right = node

    def is_leaf


class Tree:
    def __init__(self, node):
        self.root = node




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
b.left = c
a.right = d
d.left = e
T = Tree(a)


class EulerTour:
    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        self._hook_previsite(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*'  '+str(p.element()))


tour = PreorderPrintIndentedTour(T)
tour.execute()
