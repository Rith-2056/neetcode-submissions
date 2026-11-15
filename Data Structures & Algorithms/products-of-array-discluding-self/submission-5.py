class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = post * res[i]
            post = nums[i] * post
        return res