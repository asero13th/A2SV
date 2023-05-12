class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ump= Counter(words)
        res = []
        maxheap = []
        
        for key , val in ump.items():
            heappush(maxheap , [-val , key])
        for _ in range(k):
            val , key = heappop(maxheap)
            res.append(key)

        return res
    

        