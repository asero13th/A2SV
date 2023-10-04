class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i],ages[i]] for i in range(len(scores))]
        pairs.sort()
        n = len(pairs)
        dp = [pairs[i][0] for i in range(n)]
        
        for i in range(n):
            mscore, mage = pairs[i] 
            for j in range(0, i):
                score, age = pairs[j]
                if mage >= age:
                    dp[i] = max( dp[j] + mscore, dp[i])
        
   
        return max(dp)
      


                

            

        