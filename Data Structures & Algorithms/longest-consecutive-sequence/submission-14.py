class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #set to store the numbers in nums
        numSet = set(nums)
        streak = 0
        res = 0
        for num in numSet:
            if num - 1 not in numSet:
                streak = 1
                while num + streak in numSet:
                    streak += 1
            res = max(res, streak)
        return res
