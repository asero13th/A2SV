class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        nums = list(Counter(deck).values())
        check = nums[0]
        
        for num in nums:
            check = math.gcd(check, num)
            
        return all(num % check  == 0 for num in nums) and check != 1
        
        
       
        
        
        
        
        
        
        
            
        