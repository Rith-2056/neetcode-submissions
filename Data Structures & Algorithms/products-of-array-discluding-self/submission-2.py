#O(n) memory
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1] * (len(nums) + 1)
        output = []
        for num in nums:
            prefix.append(prefix[-1] * num)
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        for i in range(len(nums)):
            val = prefix[i] * postfix[i + 1]
            output.append(val)
        return output

        