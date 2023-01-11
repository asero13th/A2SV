class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words[0]
        ans = []
        hashmap = Counter(words[0])
        
        for word in words:
            word_hash = Counter(word)
            for char in hashmap:
                
                if char not in word_hash:
                    hashmap[char] = None
                elif hashmap[char] != None:
                    hashmap[char] = min(hashmap[char],word_hash[char])

        for val in hashmap:
            if hashmap[val] != None:
                ans += [val] * hashmap[val]
        return ans