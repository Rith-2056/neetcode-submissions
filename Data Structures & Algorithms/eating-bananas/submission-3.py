class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Brute force
        # for k in range(1, max(piles) + 1):
        #     hours = 0
        #     for p in piles:
        #         hours += (p + k - 1) // k
        #     if hours <= h:
        #         return k
        #Optimal soln
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            if hours <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1
        return res
                
