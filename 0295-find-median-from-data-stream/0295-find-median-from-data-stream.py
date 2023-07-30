import heapq
class MedianFinder:

    def __init__(self):
        self.mini = []
        self.maxi = []

    def addNum(self, num: int) -> None:
        if len(self.mini) == 0:        
            heapq.heappush(self.mini, -num)
        elif len(self.mini) == len(self.maxi): 
            x = self.maxi[0]
            if x < num:
                heapq.heappush(self.mini, -heapq.heappop(self.maxi))
                heapq.heappush(self.maxi, num)
            else:
                heapq.heappush(self.mini, -num)
        else:
            x = self.mini[0]
            if -x < num:
                heapq.heappush(self.maxi, num)
            else:
                heapq.heappush(self.maxi, -heapq.heappop(self.mini))
                heapq.heappush(self.mini, -num)
        return None

    def findMedian(self) -> float:
        if len(self.mini) == 0:
            return None
        if len(self.mini) > len(self.maxi):
            return -self.mini[0]
        else:
            return (-self.mini[0]+self.maxi[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()