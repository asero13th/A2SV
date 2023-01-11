class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1,n+1)]
        i = 0
        while len(circle) > 1:
            i = (i+(k - 1))%len(circle)
            circle.pop(i)
        return circle[0]
        