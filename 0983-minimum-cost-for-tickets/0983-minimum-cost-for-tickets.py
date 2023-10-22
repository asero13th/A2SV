class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        travel_days = set(days) # this creates extra space complexity
        dp = [0] * (last_day + 1) # this can be limited to O(30) with a deque
        for day in range(1, last_day + 1):
            dp[day] = dp[day - 1]
            if day in travel_days:
                dp[day] = min(
                    costs[0] + dp[max(0, day - 1)],
                    costs[1] + dp[max(0, day - 7)],
                    costs[2] + dp[max(0, day - 30)])
        return dp[-1]