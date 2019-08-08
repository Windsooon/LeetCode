# Implement Tries

# Given a list of string
# ['apple', 'app', 'bear', 'banana', 'be']

class TreeNode:
    def __init__(self, val=None, bool=False):
        self.val = val
        self.bool = bool
        self.children = {}

    def set_bool(self, bool):
        self.bool = bool

class Tries:
    def build(self, lst):
        root = {}
        self.root = TreeNode()
        for word in lst:
            self.insert(word, self.root)

    def insert(self, word, node):
        for i in range(len(word)):
            if word[i] not in node:
                node[word[i]] = TreeNode(word[i], False)
            node = node.children[word[i]]
        node.set_bool(True)

    def delete(self, word):
        stack, node = self.fast_search(word)
        stack.pop()
        while stack:
            if node.children:
                node.bool = False
                break
            else:
                parent = stack.pop()
                del parent.children[node.val]
                node = parent

    def fast_search(self, word):
        stack = []
        node = self.root
        for i in range(len(word)):
            try:
                node = node.children[word[i]]
            except KeyError:
                print('word not in the Tries')
            stack.append(node)
        return stack, node

    def search(self, word, distance):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                distance -= 1
                if distance == 0:
                    return False
                node = 1
            else:
                node = node.children[word[i]]
        return node.bool

    def level_order(self):
        if not self.root:
            return
        level = [self.root]
        while level:
            print([(node.val, node.bool) for node in level])
            tem = []
            for l in level:
                for k, v in l.children.items():
                    tem.append(v)
            level = tem

tries = Tries()
tries.build(['app', 'apt', 'apple'])
print(tries.search('app'))
tries.level_order()

