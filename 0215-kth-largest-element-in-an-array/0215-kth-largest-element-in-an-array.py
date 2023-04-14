class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def find_pivot_idx(l, r):
            pivot_idx = (l + r) // 2
            swap(pivot_idx, r)
            pivot_val = nums[r]
            end_of_larger_idx = l - 1
            for i in range(l, r):
                if nums[i] >= pivot_val:
                    swap(i, end_of_larger_idx + 1)
                    end_of_larger_idx += 1
            swap(r, end_of_larger_idx + 1)
            return end_of_larger_idx + 1
        
        def kth_largest(l, r, k):
            pivot_idx = find_pivot_idx(l, r)
            if pivot_idx - l + 1 == k:
                return nums[pivot_idx]
            elif pivot_idx - l + 1 > k:
                return kth_largest(l, pivot_idx - 1, k)
            else:
                return kth_largest(pivot_idx + 1, r, k - (pivot_idx - l + 1))
        
        N = len(nums)
        return kth_largest(0, N - 1, k)
        