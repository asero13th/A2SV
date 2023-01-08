class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l, ans = len(boxes), []
        left, right = 0, sum(i for i in range(l) if boxes[i]=='1')
        one_left, one_right = 0, boxes.count('1')
        for i in range(l):
            ans.append(left+right)
            if boxes[i]=='1':
                one_left, one_right = one_left+1, one_right-1
            left, right = left+one_left, right-one_right
        return ans
    
#         ans = [0] * len(boxes)
#         index = [i for i in range(len(boxes)) if boxes[i] == '1']

#         for idx,char in enumerate(boxes):
#             sum_of_ones  = 0
#             for val in index:
#                 sum_of_ones = sum_of_ones + abs(idx - val)
                
#             ans[idx] = sum_of_ones
#         return ans
        