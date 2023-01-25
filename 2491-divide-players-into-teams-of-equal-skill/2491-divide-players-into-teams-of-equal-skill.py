class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()
        i,j = 0, len(skill) - 1
        tmp = skill[i] + skill[j]
        while i < j:
            ans += skill[i] * skill[j]
            i,j = i + 1, j - 1
            if skill[i] + skill[j] != tmp:
                return -1            
        return ans
        
        