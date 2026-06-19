#O(26 * n)
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_arr, s2_arr = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += 1 if s1_arr[i] == s2_arr[i] else 0
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            index = ord(s2[r]) - ord('a')
            s2_arr[index] += 1
            if s1_arr[index] == s2_arr[index]:
                matches += 1
            elif s1_arr[index] + 1 == s2_arr[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2_arr[index] -= 1
            if s1_arr[index] == s2_arr[index]:
                matches += 1
            elif s1_arr[index] - 1 == s2_arr[index]:
                matches -= 1
            l += 1
        return matches == 26

        