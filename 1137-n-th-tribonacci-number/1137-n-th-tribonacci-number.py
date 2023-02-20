class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0] * 38
        arr[0] = 0
        arr[1] = 1
        arr[2] = 1
        
        for i in range(3,len(arr)):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        return arr[n]
    
        