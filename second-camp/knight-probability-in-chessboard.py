class Solution:
    MOVES = (
        (1, 2), (1, -2),
        (2, 1), (2, -1),
        (-1, 2), (-1, -2),
        (-2, 1), (-2, -1),
    )

    def knightProbability(self, n: int, moves: int, start_row: int, start_col: int) -> float:
        @cache
        def dp(i: int, j: int, k: int) -> float:
            if not (0 <= i < n) or not (0 <= j < n):
                return 0.0
            if k <= 0:
                return (1 / len(self.MOVES)) ** moves
            return sum(dp(i + di, j + dj, k - 1) for di, dj in self.MOVES)

        return dp(start_col, start_row, moves)