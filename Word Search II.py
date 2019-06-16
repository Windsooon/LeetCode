class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.is_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        # word
        current = self.root
        for w in word:
            # {w: TrieNode()}
            if w not in current.childrens:
                current.childrens[w] = TrieNode()
            current = current.childrens[w]
        current.is_word = True

class Solution:
    def findWords(self, board, words):
        if not words:
            return []
        trie = Trie()
        for w in words:
            trie.insert(w)
        self.res = []
        for word in words:
            for x in range(len(board)):
                for y in range(len(board[0])):
                    self.search(trie.root, x, y, '', board)
        return self.res

    def search(self, node, x, y, path, board):
        # 0, 0, 0, board, oath
        if node.is_word:
            self.res.append(path)
            node.is_word = False
        if x < 0 or y < 0 or x > len(board)-1 or y > len(board[0])-1:
            return False
        if board[x][y] not in node.childrens:
            return False
        else:
            node = node.childrens[board[x][y]]
        tem = board[x][y]
        board[x][y] = '#'
        self.search(node, x, y+1, path+tem, board)
        self.search(node, x+1, y, path+tem, board)
        self.search(node, x-1, y, path+tem, board)
        self.search(node, x, y-1, path+tem, board)
        board[x][y] = tem


board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
# board = [["a","a"]]
# words = ["aaa"]
# words = ["oath"]

# board = [
#     ["a","b","c"],
#     ["a","e","d"],
#     ["a","f","g"]]
# 
# words = ["eaabcdgfa"]

board = [['a']]
words = ['a']

s = Solution()
print(s.findWords(board, words))
