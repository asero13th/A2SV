class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        lossers = {}
        ans = [[]] * 2
        for idx,val in enumerate(matches):
            if val[0] in winners: winners[val[0]].append(idx)
            else: winners[val[0]] =  [idx]
                
            lossers[val[1]] = lossers.get(val[1],0) + 1
                
        tmp_winners = [key for key in winners if key not in lossers]     
        tmp_lossers = [key for key in lossers if lossers[key] == 1 ]

        tmp_winners.sort()
        tmp_lossers.sort()
        
        ans[0] = tmp_winners
        ans[1] = tmp_lossers
        
        return ans