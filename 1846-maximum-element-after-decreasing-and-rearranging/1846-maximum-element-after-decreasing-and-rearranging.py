class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for i, val in enumerate(arr):
            if i == 0:
                arr[i] = 1
            
            else:
                if arr[i] - arr[i - 1] > 1:
                    arr[i] = arr[i - 1] + 1
        return max(arr)