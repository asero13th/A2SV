class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backTrack(idx, arr, curr):
            
            if curr == 0:
                ans.append((arr.copy()))
            else:

                for i in range(idx, len(candidates)):

                    if(i != idx and candidates[i-1] == candidates[i]):  # remove the duplicates
                            continue

                    if(curr < candidates[i]):
                            break



                    backTrack(i + 1, arr + [candidates[i]] , curr - candidates[i])
            
              
            
        ans = []
        candidates.sort()   
        backTrack(0, [], target)
        return ans
                
        
            
        