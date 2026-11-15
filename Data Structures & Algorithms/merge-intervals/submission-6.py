class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        first = intervals[0]
        for start, end in intervals[1:]:
            if first[-1] >= start:
                first[-1] = max(first[-1], end)
            else:
                merged.append(first)
                first = [start, end]
        merged.append(first)
        return merged


