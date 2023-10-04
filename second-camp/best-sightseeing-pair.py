class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_value = 0
        max_prev = values[0]


        for i in range(1, n):
            max_value = max(max_value, values[i] + max_prev - i)
            max_prev = max(max_prev, values[i] + i)
        return max_value
        