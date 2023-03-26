class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def helper(nums, i, subset, output):
            
            
            output.append(subset.copy())
                
            
            for j in range(i, len(nums)):
                
                subset.append(nums[j])
                helper(nums, j + 1 ,subset,output)
                subset.pop()

        helper(nums,0,[],output)
        return output
                
            