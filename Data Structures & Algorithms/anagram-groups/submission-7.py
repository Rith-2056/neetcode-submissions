#O(nlog(n))
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyToValue = collections.defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            keyToValue[sortedS].append(s)
        return list(keyToValue.values())
            
