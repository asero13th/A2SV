class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_idx = sorted(list(range(len(intervals))), key = lambda x: intervals[x][0])
        ans = []
        for start, end in intervals:
            
            left, right = 0, len(sorted_idx) - 1
            
            while left <= right:
                
                middle = (left + right) //2
                idx = sorted_idx[middle]
                
                if intervals[idx][0] < end:
                    left = middle + 1
                else:
                    right = middle - 1
                    
            ans.append(sorted_idx[left]) if left < len(intervals) else ans.append(-1)
        return ans
            
                
                
        
        
        
        