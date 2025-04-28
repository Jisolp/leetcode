class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackIdx = stack.pop() 
                res[stackIdx] = (idx-stackIdx)
            stack.append([temp,idx])
        return res