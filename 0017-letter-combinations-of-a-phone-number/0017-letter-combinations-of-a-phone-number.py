class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        alphas = ['','',"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def backtrack(i, arr):
            if len(arr) == len(digits):
                ans.append("".join(arr))
                return
            
            
            
            for j in range(i, len(digits)):
                idx = int(digits[j])
                for k in range(len(alphas[idx])):
                
                    arr.append(alphas[idx][k])
                    backtrack(j + 1 , arr)
                    arr.pop()
                    
        backtrack(0,[])       
        return ans