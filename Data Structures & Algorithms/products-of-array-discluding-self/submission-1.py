class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        zero_count = nums.count(0)
        if zero_count > 1:
            return res
        
        #product of non-zero elements
        total = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                total = total * nums[i]
        
        if zero_count == 1:
            for idx, val in enumerate(nums):
                if val==0:
                    res[idx] = total
                    break
            return res
        
        #no zeros
        for idx, val in enumerate(nums):
            res[idx] = total//val
        return res