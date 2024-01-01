class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = 0
        def binarySearch(k=-1):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] == k:
                    return left+mid
                elif arr[mid] < k:
                    left = mid+1
                else:
                    right = mid - 1
            return -1

        while k:
            counter += 1
            index = binarySearch(counter)
            if not (index+ 1):
                k -= 1
        return counter