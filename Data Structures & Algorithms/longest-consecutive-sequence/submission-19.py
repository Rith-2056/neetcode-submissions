class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        streak = 0
        maxStreak = 0
        for n in num:
            if n - 1 not in num:
                streak = 1
                while n + streak in num:
                    streak += 1
                maxStreak = max(maxStreak, streak)
        return maxStreak
        