class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root=TrieNode()

        for f in folder:
            components=f.strip("/").split("/")
            node=root
            for c in components:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_end=True

        def dfs(node,components):
            if node.is_end:
                return False if len(components)>0 else True
                
            return dfs(node.children[components[0]],components[1:])

        ans=[]
        
        for f in folder:
            components=f.strip("/").split("/")
            if dfs(root,components):
                ans.append(f)

        return ans