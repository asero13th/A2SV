class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        comment = False
        ans = []
        tmpStr = ""
        for code in source:
            if not comment: tmpStr = ""
            i = 0
            
            while i < len(code):
                if comment:
                    if i + 1 < len(code)  and code[i:i + 2] == '*/':
                        comment = False
                        i += 2
                        continue
                    i += 1
                else:
                    if code[i:i + 2] == '/*' and i + 1 < len(code):
                        comment = True
                        i += 2
                        continue
                    if code[i:i + 2] == '//':
                        break
                    tmpStr += code[i]
                    i += 1
            if tmpStr and not comment:
                ans.append(tmpStr)
        return ans
                
        
        
        