class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            if cnt > 1:
                return num