class TrieNode():
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end=True

    def search(self, word: str) -> bool:

        def dfs(node,index):
            if index == len(word):
                return node.is_end

            c = word[index]

            if c not in node.children:
                return False
            return dfs(node.children[c],index+1)

        return dfs(self.root,0)

    def startsWith(self, prefix: str) -> bool:
        def dfs(node,index):
            if index == len(prefix):
                if node.children:
                    return True
                return node.is_end
            
            c=prefix[index]

            if c not in node.children:
                return False
            return dfs(node.children[c],index+1)
        return dfs(self.root,0)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)