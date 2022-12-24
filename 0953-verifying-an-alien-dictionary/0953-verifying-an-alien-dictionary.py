class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        val = 1
        for s in order:
            hashmap[s] = val
            val += 1
        
        for idx,word in enumerate(words):
            i = 0
            flag = 0
            if  idx < len(words) - 1:
                tmp = words[idx + 1]
                while i < (min(len(word),len(tmp))):
                    if hashmap[word[i]] < hashmap[tmp[i]]:
                        flag = 1
                        i += 1
                        break
                    if hashmap[word[i]] > hashmap[tmp[i]]:
                        print(word[i],tmp[i])
                        return False
                    i += 1
                    
                if len(word) > len(tmp) and not flag:
                    return False
                    
                    
        return True
                    
    