class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        ans = 0
        for right,char in enumerate(s):
            hashmap[char] = hashmap.get(char,0) + 1
            
            while left < right and hashmap[char] > 1 :
                hashmap[s[left]] -= 1
                
                if hashmap[s[left]] == 0:
                    hashmap.pop(s[left])
                left += 1
            if len(hashmap) == right - left + 1:
                    ans  = max(ans,len(hashmap))
            
        return ans
                
        