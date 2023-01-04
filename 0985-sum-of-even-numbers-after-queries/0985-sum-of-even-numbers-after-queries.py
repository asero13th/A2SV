class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        seg = [0]*4*len(nums)
        def build(idx,lo,hi):
            if lo == hi:
                if nums[lo]%2 == 0:
                    seg[idx] = nums[lo]
                return
            mid = (lo+hi)//2
            build(2*idx+1,lo,mid)
            build(2*idx+2,mid+1,hi)
            seg[idx] = seg[2*idx+1]+seg[2*idx+2]
        def update(idx,lo,hi,i,val):
            if lo == hi:
                seg[idx] = val
                return
            mid = (lo+hi)//2
            if i <= mid:
                update(2*idx+1,lo,mid,i,val)
            else:
                update(2*idx+2,mid+1,hi,i,val)
            seg[idx] = seg[2*idx+1]+seg[2*idx+2]
            
        
        #just for the sake of segment tree completeness
        def query(idx,lo,hi,l,r):
            if r < lo or l > hi:
                return 0
            if l >= lo and r <= hi:
                return seg[idx]
            mid = (lo+hi)//2
            return query(2*idx+1,lo,mid,l,r)+query(2*idx+2,mid+1,hi,l,r)
        stored = [0 for _ in range(len(nums))]
        ans = []
        build(0,0,len(nums)-1)
        for i,j in queries:
            val = nums[j]+i
            if val%2 == 0:
                update(0,0,len(nums)-1,j,val)
            else:
                update(0,0,len(nums)-1,j,0)
            ans += [seg[0]]
            nums[j] += i
        return ans
#         ans = []
#         evensum = sum(v for v in nums if v % 2 == 0)
        
#         for val, idx in queries:
#             num = nums[idx]
#             if num % 2 == 0: evensum  -= num
                
#             nums[idx] += val
            
#             if nums[idx] % 2 == 0: evensum += nums[idx]
                
#             ans.append(evensum)
            
#         return ans