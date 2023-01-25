class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)
        hashmap = {}
        ans = []
        l = 0
        
        for i,v in enumerate(s):
            hashmap[v] = hashmap.get(v,c[v]) - 1
            
            if hashmap[v] == 0:
                hashmap.pop(v)
                
            if len(hashmap)  == 0:
                ans.append(i - l + 1)
                l = i + 1
        return ans
                
                
        