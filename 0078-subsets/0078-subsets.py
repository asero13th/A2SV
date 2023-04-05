class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def helper(nums, index, subset, output):
            
            
            output.append(subset.copy())   
            
            for i in range(index, len(nums)):
                
                subset.append(nums[i])
                helper(nums, i + 1 ,subset,output)
                subset.pop()

        helper(nums,0,[],output)
        return output
                
            