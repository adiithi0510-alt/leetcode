class Solution:
    def pathsWithMaxScore(self, board):
        n = len(board)
        MOD = 10**9 + 7
        dp = [[(-1, 0)] * n for _ in range(n)]  # (maxSum, count); -1 = unreachable
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                c = board[i][j]
                if c == 'X':
                    continue
                if i == n - 1 and j == n - 1:  # 'S'
                    dp[i][j] = (0, 1)
                    continue
                
                best, cnt = -1, 0
                for di, dj in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n and dp[ni][nj][0] != -1:
                        s = dp[ni][nj][0]
                        if s > best:
                            best, cnt = s, dp[ni][nj][1]
                        elif s == best:
                            cnt = (cnt + dp[ni][nj][1]) % MOD
                
                if best == -1:
                    continue
                val = 0 if c in ('E', 'S') else int(c)
                dp[i][j] = (best + val, cnt)
        
        if dp[0][0][0] == -1:
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1] % MOD]