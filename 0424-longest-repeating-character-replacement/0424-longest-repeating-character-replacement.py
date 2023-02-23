class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        maximum = 0
        ans = 0
        for right, char in enumerate(s):
            hashmap[char] = hashmap.get(char, 0) + 1
            maximum = max(maximum, hashmap[char])
            while right - left + 1 > maximum + k :
                hashmap[s[left]] -= 1
                
                if hashmap[s[left]] == 0:
                    hashmap.pop(s[left])
                left += 1
            ans = max(ans,right -left + 1)
        return ans
                