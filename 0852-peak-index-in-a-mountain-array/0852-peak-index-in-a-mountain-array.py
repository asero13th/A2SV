class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0,len(arr)-1
        while(l<r):
            mid = (l+r)//2
            peak = arr[mid]
            if arr[mid-1]<peak and arr[mid+1]<peak:
                return mid
            elif arr[mid-1]<peak and arr[mid+1]>peak:
                l = mid
            elif arr[mid-1]>peak and arr[mid+1]<peak:
                r = mid
        return l
                
            