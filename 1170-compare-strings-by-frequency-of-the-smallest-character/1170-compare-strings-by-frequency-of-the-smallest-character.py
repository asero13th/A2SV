class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
      
           
        words.sort(key=lambda x: self.f(x))
        ans = []
        print(words)
        for query in queries:
            left, right = 0 , len(words) - 1
            while left <= right:
                middle = (left + right) //2
                if self.f(words[middle]) > self.f(query):
                    right = middle - 1
                else:
                    left = middle + 1
            ans.append(len(words) - left)
        return ans
    
    def f(self,string):
        new_string = list(string)
        new_string.sort()
        C = Counter(string)
        return C[new_string[0]]
        
            
            
    
        