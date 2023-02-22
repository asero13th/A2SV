class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        hashmap = {}
        ans = []
        left = 0
    
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i],0) + 1
            if hashmap == target:
                ans.append(left)

            if i - left + 1 == len(p):
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    hashmap.pop(s[left])
                left += 1
            
        return  ans
    
        