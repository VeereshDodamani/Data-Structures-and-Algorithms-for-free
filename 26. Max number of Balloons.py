# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
# Leetcode problem: 1189

from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = "balloon"

        for c in text:
            if c in balloon:
                counter[c] += 1

        if any(counter[c] == 0 for c in balloon):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])

text = "nlaebolko"
sol = Solution()
print(sol.maxNumberOfBalloons(text)) 
