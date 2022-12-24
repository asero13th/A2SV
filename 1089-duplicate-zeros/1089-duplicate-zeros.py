class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        
        """
        i = 0
        while i < len(arr):

            j = len(arr) - 1
            
            if arr[i] == 0:
                
                while j > i:
                    arr[j] = arr[j - 1]
                    j -= 1
                
                i += 1
            i += 1
        
                
            
            