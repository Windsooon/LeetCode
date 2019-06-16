import collections

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


    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for w in word:
            if w in current.childrens:
                current = current.childrens[w]
            else:
                return False
        return current.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for w in prefix:
            if w in current.childrens:
                current = current.childrens[w]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple");
assert trie.search("apple") is True
assert trie.search("app") is False
assert trie.startsWith("app") is True
trie.insert("app");
assert trie.search("app") is True
