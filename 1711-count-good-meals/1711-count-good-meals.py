class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers_of_2 = [2 ** i for i in range(22)]
        c = Counter()
        ans = 0
        for d in deliciousness:
            for pw in powers_of_2:
                ans += c[pw - d]
            c[d] += 1
        return ans % ((10 ** 9) + 7)
        
            
            
        
        