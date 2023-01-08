class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        index = [i for i in range(len(boxes)) if boxes[i] == '1']

        for idx,char in enumerate(boxes):
            sum_of_ones  = 0
            for val in index:
                sum_of_ones = sum_of_ones + abs(idx - val)
                
            ans[idx] = sum_of_ones
        return ans
        