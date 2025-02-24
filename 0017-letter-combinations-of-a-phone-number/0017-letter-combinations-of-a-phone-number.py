import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits)==0:
            return ans

        def backtrack(index, current_combination):
            if index == len(digits):
                ans.append(current_combination)
                return
            
            letters = digit_to_letters[digits[index]]

            for letter in letters:
                backtrack(index+1, current_combination+letter)

        backtrack(0,"")

        return ans
