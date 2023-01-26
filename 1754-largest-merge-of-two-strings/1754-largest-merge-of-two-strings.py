class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        i,j = 0,0
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                    merge.append(word1[i])
                    i += 1
            elif word1[i] < word2[j]:
                    merge.append(word2[j])
                    j += 1
            else:
                if word1[i:len(word1)] > word2[j:len(word2)]:
                    merge.append(word1[i])
                    i += 1
                else:
                    merge.append(word2[j])
                    j += 1
        
        merge.extend(word1[i:len(word1)])
        merge.extend(word2[j: len(word2)])
        return "".join(merge)
                    
                    
                    
                    
        