class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
  
        return [j[0] for i, j in enumerate(Counter(nums).most_common()) if i < k]

       
        