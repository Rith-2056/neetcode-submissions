class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0      # Tracks the highest streak overall
        longest = 0  # Tracks the current streak of 1s
        
        for num in nums:
            if num == 1:
                longest += 1
                res = max(res, longest) # Update the highest streak
            else:
                longest = 0 # Reset current streak when hitting a 0
                
        return res