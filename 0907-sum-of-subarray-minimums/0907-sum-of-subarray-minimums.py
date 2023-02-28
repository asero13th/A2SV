class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        
        range_sum = [[i,len(arr) - 1] for i in range(len(arr))]
        
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                index = stack.pop()
                range_sum[index][1] = i-1
                range_sum[i][0] = range_sum[index][0]  
            stack.append(i)
        
        for i, nums in enumerate(range_sum):
            left , right = nums[0],nums[1]
            left_sum =  i - left + 1
            right_sum =  right - i + 1
            
            times = left_sum * right_sum
            ans += (arr[i] * times)
        print(range_sum)
        return ans % (10**9 + 7)
        
        
             
            
            
        