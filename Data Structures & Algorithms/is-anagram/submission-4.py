from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for letter in range(len(s)):
            s_dict[s[letter]] += 1
        for letter in range(len(t)):
            t_dict[t[letter]] += 1
        return s_dict == t_dict
        