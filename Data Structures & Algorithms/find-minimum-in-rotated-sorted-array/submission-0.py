class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        for i in range(len(nums)):
            if minNum > nums[i]:
                minNum = nums[i]
            else:
                minNum = minNum
        return minNum