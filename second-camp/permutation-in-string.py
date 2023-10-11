class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashmap_s1 = {}
        hashmap_s2  = {}
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            hashmap_s1[char] = 0
            hashmap_s2[char] = 0
       
        for i in range(len(s1)):
            hashmap_s1[s1[i]] += 1
            hashmap_s2[s2[i]] += 1
        
        
        for val in hashmap_s1:
                if hashmap_s1[val] != hashmap_s2[val]:
                    break
        else:
            return True
        
        
        i,j = 1,len(s1)
        while j < len(s2):
               
            hashmap_s2[s2[i - 1]] -= 1
            hashmap_s2[s2[j]] += 1
            
            for val in hashmap_s1:
                if hashmap_s1[val] != hashmap_s2[val]:
                    break
            else:
                return True
            
            i += 1
            j += 1
            
            
        return False
        
        
            