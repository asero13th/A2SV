class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []
        for path in paths:
            files = path.split()
            
            for idx, file in enumerate(files):
                if idx != 0:
                    i,j = file.find('('), file.find(')')
                    
                    file_name = file[i + 1:j]
                    if file_name in hashmap:
                        hashmap[file_name].append(files[0] + '/' + file[0:i])
                    else:
                        hashmap[file_name] = [files[0] + '/' + file[0:i]]
                    
        for file in hashmap:
            if len(hashmap[file]) > 1:
                ans.append(hashmap[file])
        return ans
                    
                    
                    
                
                
        
                
            
            