class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        replace_map = defaultdict(list)

        for idx,src,tgt in zip(indices, sources, targets):
            replace_map[idx].append((src,tgt))

        res=[]
        i=0

        while i<len(s):
            replaced=False
            if i in replace_map:
                for src, tgt in replace_map[i]:
                    if s[i:i+len(src)]==src:
                        res.append(tgt)
                        i+=len(src)
                        replaced=True
                        break
            if not replaced:               
                res.append(s[i])    
                i+=1
        
        return ''.join(res)