from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_s = defaultdict(int)
        letter_t = defaultdict(int)
        for letter in s:
            letter_s[letter] += 1
        for letter in t:
            letter_t[letter] += 1
        return letter_s == letter_t