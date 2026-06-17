class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            cArea = min(heights[left], heights[right]) * (right-left)
            mArea = max(mArea, cArea)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return mArea