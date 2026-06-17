from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        for counter in count.values():
            if counter > 1:
                return True
        return False