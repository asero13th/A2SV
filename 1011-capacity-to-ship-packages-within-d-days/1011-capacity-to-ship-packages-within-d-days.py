class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        
        
        def isValid(w):
            count = 0
            temp = 0
            for i in weights:
                temp += i
                if(temp > w):
                    count += 1
                    temp = i
                if(count > days):
                    return 0
            count += 1
            return count <= days
        l, r = max(weights), sum(weights)
        while(l <= r):
            mid = (l+r)//2
            if(isValid(mid)):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans