from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastNum = output[-1][1]
            if start <= lastNum:
                output[-1][1] = max(lastNum, end)
            else:
                output.append([start,end])
        return output
