# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        left, right = [], []
        for i in range(len(intervals)):
            if intervals[i].end < start:
                left.append(intervals[i])
        for i in range(len(intervals)):
            if intervals[i].start > end:
                right.append(intervals[i])
        if left + right != intervals:
            start = min(start, intervals[len(left)].start)
            end = max(end, intervals[-len(right)-1].end)
        return left + [Interval(start, end)] + right
