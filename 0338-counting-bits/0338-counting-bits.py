class Solution:
    def countBits(self, n: int) -> List[int]:
        index = [0,1,1,2]
        
        if n < len(index):
            return index[:n+1]
        prev = 4
        for i in range(4,n + 1):
            
            if i & i - 1 == 0:
                prev = i
                index.append(1)
            else:
                index.append(1 + index[i - prev])
        return index
                
            
            
        
        
        
        
        
                
                
        