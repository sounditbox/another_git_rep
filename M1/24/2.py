from typing import List


class Solution:
    dig = {
        '2': set('abc'),
        '3': set('def'),
        '4': set('ghi'),
        '5': set('jkl'),
        '6': set('mno'),
        '7': set('pqrs'),
        '8': set('tuv'),
        '9': set('wxyz'),
    }

    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        self.rec_add_letter('', digits, answer)
        return answer

    def rec_add_letter(self, prefix, digits, answer) -> None:
        if not digits:
            answer.append(prefix)
            return
        ls = self.dig[digits[0]]
        for l in ls:
            self.rec_add_letter(prefix + l, digits[1:], answer)

s = Solution()
print(s.letterCombinations('23'))