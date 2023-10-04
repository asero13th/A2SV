class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):  # Consider 31-bit integers (signed integers in Python)
            mask |= (1 << i)
            prefix_set = set()
            for num in nums:
                prefix_set.add(num & mask)
            
            possible_max = max_xor | (1 << i)
            for prefix in prefix_set:
                if (prefix ^ possible_max) in prefix_set:
                    max_xor = possible_max
                    break
        return max_xor

            