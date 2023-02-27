class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        ans = 0
        while tickets[k] != 0:
            i = i %len(tickets)
            tickets[i] -= 1
            
            if tickets[i] >= 0:
                ans += 1
            i += 1
            
        return ans
        
        