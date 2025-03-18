class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letter=set()

        for c in s:
            if c in letter:
                letter.remove(c)
            else:
                letter.add(c)

        return len(letter) <= 1