#One pass
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1] * (len(nums))
        cur_prod = 1
        res = []
        for i in range(len(nums)):
            product = nums[i] * prefix[i]
            prefix.append(product)
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = cur_prod
            cur_prod = cur_prod * nums[i]
        for i in range(len(postfix)):
            product = prefix[i] * postfix[i]
            res.append(product)
        return res

        
        