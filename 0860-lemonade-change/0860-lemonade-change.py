class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ans = 0
        hashmap = {5 : 0, 10 : 0, 20: 0}
        
        for i, bill in enumerate(bills):
            if bill == 5:
                hashmap[5] += 1
                
            if bill == 10:
                hashmap[10] += 1
                hashmap[5] -= 1
      
            if bill == 20:
                hashmap[20] += 1
                if hashmap[10]:
                    hashmap[10] -= 1
                else:
                    hashmap[5] -= 2
                hashmap[5] -= 1
                
            if  hashmap[5] < 0:
                return False
                
                
               
           
        return True
        