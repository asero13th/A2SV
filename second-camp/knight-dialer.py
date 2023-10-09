class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        hashmap = {
            0 : 2,  1 : 2, 2 : 2, 3 : 2, 4 : 3, 5: 0, 6 : 3, 7: 2, 8: 2, 9: 2
        }

        pair = {
            0 : [6, 4],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6 : [0, 1, 7],
            7 : [6, 2],
            8 : [1, 3],
            9: [2, 4]
        }

        dp = [[0 for _ in range(10)] for _ in range(n)]
        
        for i in range(1, n):
            for j in range(10):
                if i  == 1:
                    dp[i][j] += hashmap[j]
                else:
                    for x in pair[j]:
                        dp[i][j] += dp[i - 1][x]
                
    
        ans = sum(dp[n - 1])
        # print(dp)
        return ans % ((10 ** 9) + 7)
