class Solution:
    def _counting(self,word:str,k:int) -> int:
        count=0
        l=r=0
        vowels={'a','e','i','o','u'}
        vowel_count={}
        consonant=0

        while r<len(word):
            c=word[r]

            if c in vowels:
                if c not in vowel_count:
                    vowel_count[c]=1
                else:
                    vowel_count[c]+=1
            else:
                consonant+=1

            while len(vowel_count)==5 and consonant>=k:
                count += len(word)-r
                start=word[l]
                if start in vowels:
                    vowel_count[start]-=1
                    if vowel_count[start]==0:
                        del vowel_count[start]
                else:
                    consonant-=1
                l+=1

            r+=1

        return count

    def countOfSubstrings(self, word: str, k: int) -> int:

        return self._counting(word,k) - self._counting(word,k+1)