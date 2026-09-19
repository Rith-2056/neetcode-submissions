class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sumOfNum = nums[l] + nums[r] + nums[i]
                if sumOfNum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate values for r
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sumOfNum < 0:
                    l += 1
                else:
                    r -= 1
        return res
            

