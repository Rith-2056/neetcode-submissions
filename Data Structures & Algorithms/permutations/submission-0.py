class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sublist = []
        def dfs():
            if len(sublist) == len(nums):
                res.append(sublist.copy())
                return
            for x in nums:
                if x not in sublist:
                    sublist.append(x)
                    dfs()
                    sublist.pop()
        dfs()
        return res