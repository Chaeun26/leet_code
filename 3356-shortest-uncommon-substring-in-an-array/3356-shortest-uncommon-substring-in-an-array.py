class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n=len(arr)
        substrings=defaultdict(set)

        for i,word in enumerate(arr):
            lenW=len(word)
            for j in range(1,lenW+1):
                for k in range(lenW-j+1): 
                    sub=word[k:k+j]
                    substrings[sub].add(i)
        res=[]
        for i,word in enumerate(arr):
            min_substring=""
            lenW=len(word)
            for j in range(1,lenW+1):
                for k in range(lenW-j+1):
                    sub=word[k:k+j]
                    if substrings[sub]=={i}:
                        if not min_substring or sub<min_substring:
                            min_substring=sub
                if min_substring:
                    break
            res.append(min_substring)
        
        return res