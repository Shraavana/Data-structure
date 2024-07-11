class TrieNode:
    def __init__(self) :
        self.children={}
        self.is_end=False
class SuffixTrie:
    def __init__(self):
        self.root=TrieNode()
    def suffix(self,word):
        for i in range(len(word)):
            self.insert(word[i:])
    def insert(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current = current.children[char]
        current.is_end = True
    
    def search(self,word):
        current=self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
suffix_trie = SuffixTrie()
suffix_trie.suffix("mannan")
print(suffix_trie.search("ana"))
print(suffix_trie.search("annan"))
print(suffix_trie.search("nan"))

