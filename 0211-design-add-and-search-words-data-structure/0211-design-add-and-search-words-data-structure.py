class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
                
        def dfs(node,index):
            if index == len(word):
                return node.is_end

            c = word[index]

            if c == '.':
                for c2 in node.children.values():
                    if dfs(c2,index+1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c],index+1)
        
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)