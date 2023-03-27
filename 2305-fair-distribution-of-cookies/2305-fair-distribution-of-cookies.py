class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        fairness = sum(cookies)
        children = [0] * k
        cookies.sort(reverse = True)
        def backtrack(arr, index):
            nonlocal fairness
            
            if index >= len(cookies):
                fairness = min(fairness, max(arr))
                return
            
            
            if max(arr) >= fairness:
                    return
                    
            for i in range(k):
                
                
                arr[i] += cookies[index]
                
                backtrack(arr, index + 1)
                arr[i] -= cookies[index]
                
        backtrack(children,0)
        return fairness
    