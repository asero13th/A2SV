class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        if arr[1] <= arr[0]:
            return False
        decrease = False
        
        for i in range(1,len(arr)):
            if not decrease and  arr[i] < arr[i -1]:
                decrease =  True
                
            if decrease and arr[i] > arr[i - 1] or arr[i] == arr[i - 1]:
                return False
        
        return decrease == True