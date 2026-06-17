from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count, count2 = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            count2[t[i]] += 1
        return count == count2