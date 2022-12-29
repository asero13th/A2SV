class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        ans = []
        for string in cpdomains:
            tmpStr = string.split()
            domain = tmpStr[1].split('.')
            
            tmp = ""
            for i in range(len(domain) - 1,-1,-1):
                tmp = domain[i] + '.' + tmp if i != len(domain) - 1 else domain[i]
                
                hashmap[tmp] = hashmap.get(tmp,0) + int(tmpStr[0])
        for key in hashmap:
            ans.append(str(hashmap[key]) + " " + key)
            
        return (ans)
            
                
                    
                
                
            
            
            
            
            
            