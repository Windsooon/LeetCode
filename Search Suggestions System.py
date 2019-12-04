class Trie:
    def __init__(self):
        self.children = dict()
        self.words = []
        
class Solution:
    def suggestedProducts(self, products, searchWord: str):
        root = Trie()
        self.buildtries(root, products)
        return self.search_word(root, searchWord)
    
    def buildtries(self, root, products):
        for p in products:
            self.add_word(root, p)
    
    def add_word(self, root, word):
        current = root
        for w in word:
            current.words.append(word)
            if w not in current.children:
                current.children[w] = Trie()
            current = current.children[w]
        current.words.append(word)

    def search_word(self, root, word):
        current = root
        res = []
        for w in word:
            if w in current.children:
                res.append(sorted(current.children[w].words)[:3])
            current = current.children[w]
        return res

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"

s = Solution()
print(s.suggestedProducts(products, searchWord))
