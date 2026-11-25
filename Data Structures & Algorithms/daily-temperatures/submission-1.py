class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #(val, i)
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                cur_temp, cur_index = stack.pop()
                res[cur_index] = i - cur_index
            stack.append((t, i))
        
        return res
                