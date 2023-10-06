class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for x, y in costs:
            diff.append([x - y,[x, y]])
        diff.sort()
        i, j = 0, len(costs) - 1
        ans = 0
        while i < j:
            ans += diff[i][1][0]
            ans += diff[j][1][1]
            i += 1
            j -= 1
        return ans
        