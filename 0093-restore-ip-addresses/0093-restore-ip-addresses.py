class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start: int, dots: int, ip: str, result: List[str]) -> None:
            if start == len(s) and dots == 4:
                result.append(ip[:-1])
                return
            
            for i in range(start, min(start + 3, len(s))):
                segment = s[start:i+1]
                if len(segment) > 1 and segment[0] == '0':
                    continue
                if 0 <= int(segment) <= 255 :
                    backtrack(i+1, dots+1, ip + segment + '.', result)
                
        result = []
        backtrack(0, 0, '', result)
        return result
        