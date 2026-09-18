#O(n) solution

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        streak = 0
        res = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                streak = 1
                while num + streak in nums_set:
                    streak += 1
                res= max(streak, res)

        return res
