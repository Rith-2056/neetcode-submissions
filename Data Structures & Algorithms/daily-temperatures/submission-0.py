#Brute force

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for idx in range(len(temperatures)):
            for idx2 in range(idx + 1, len(temperatures)):
                if temperatures[idx2] > temperatures[idx]:
                    res[idx] = idx2 - idx
                    break

        return res
            

