class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def helper(nums, i, subset, output):
            if i == len(nums):
                output.append(subset[:])
                return 

            val = nums[i]

            # Take value.
            subset.append(val)
            helper(nums, i + 1, subset, output)
            subset.pop()

            # Skip value.
            helper(nums, i + 1, subset, output)
        helper(nums, 0, [], output)
        return output