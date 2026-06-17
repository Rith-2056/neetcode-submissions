from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            son = numbers[l] + numbers[r]
            if son > target:
                r -= 1
            elif son < target:
                l += 1
            else:
                return [l + 1, r + 1]
            
        
        