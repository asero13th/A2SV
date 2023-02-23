class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        if len(arr) <= 2 and len(c) == 2:
            return len(arr)
        if len(arr) <= 2 or len(c) == 1:
            return 1
        
        left = 0
        ans = 0
        for i in range(2, len(arr)):
            prevous = arr[i - 1] - arr[i - 2]
            current = arr[i] - arr[i - 1]
            
            if current * prevous > 0 or  prevous == 0:
                left = i - 1
                
            elif current == 0:
                ans = max(ans,2)
                left = i                
            
            ans = max(ans, i - left + 1)
        return ans 
            
            
            
            
            
        