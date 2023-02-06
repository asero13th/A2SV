class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * len(nums1)
        
        #sortig the index of the array using the value
        index = sorted(range(len(nums2)),key=lambda x:nums2[x], reverse=True)
        
        #hold the value if the value at both index the same or less
        remaining = []
        
        for a in sorted(nums1):
            if a > nums2[index[-1]]:
                ans[index.pop()] = a
            else:
                remaining.append(a)

        for b, a in zip(index, remaining):
            ans[b] = a
        return ans