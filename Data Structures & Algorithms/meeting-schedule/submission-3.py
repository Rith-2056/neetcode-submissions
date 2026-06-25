#Brute force
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        for i in range(len(intervals)):
            interval = intervals[i]
            for j in range(i + 1, len(intervals)):
                two_int = intervals[j]
                if interval.end > two_int.start:
                    return False
        return True
            