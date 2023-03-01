class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        return [1, *self.getsum(self.getRow(rowIndex - 1)),1]
    
    def getsum(self,arr):
        ans = []
        for i in range(len(arr) - 1):
            ans.append(arr[i] + arr[i + 1])
        return ans 
    