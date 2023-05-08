class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board = board[::-1]
        B = []
        visited = set()
        visited.add(1)
        for i in range(n):
            if i%2==0:
                B += board[i]
            else:
                B += board[i][::-1]
        queue = [1]
        steps = 0
        while queue:
            for _ in range(len(queue)):
                q = queue.pop(0)
                for i in range(q+1,q+7):
                    if B[i-1]!=-1 and B[i-1] not in visited:
                        if B[i-1]==n**2:
                            return steps + 1
                        queue.append(B[i-1])
                        visited.add(B[i-1])
                    elif B[i-1]==-1 and i not in visited:
                        if i == n**2:
                            return steps + 1
                        queue.append(i)
                        visited.add(i)
            steps += 1
        return -1
        