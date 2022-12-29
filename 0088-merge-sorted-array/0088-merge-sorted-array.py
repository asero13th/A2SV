class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = [nums1[i] for i in range(m)]
        i,j,k = m  - 1,n - 1,len(nums1) - 1
        
        while i >= 0 and j >= 0:
            
            nums1[k] = max(tmp[i],nums2[j])
            if tmp[i] >= nums2[j]: i -= 1
            else: j -= 1
            
            k -= 1
            
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        while i >= 0:
            nums1[k] = tmp[i]
            i -= 1
            k -= 1
            
            