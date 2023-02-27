class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        x = tickets[k]
        ans = 0
        
        for i in range(k + 1):
            ans += min(x, tickets[i])
        
        for i in range(k + 1, len(tickets)):
            ans += min (x - 1, tickets[i])
        return ans
        
        