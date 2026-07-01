from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # Step 1: Multi-source BFS to compute min distance to any thief
        dist = [[-1] * n for _ in range(n)]
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # Step 2: Binary search on safeness factor k
        # Check if path exists where every cell has dist >= k
        def canReach(k):
            if dist[0][0] < k or dist[n-1][n-1] < k:
                return False
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= k:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False

        lo, hi = 0, n * 2  # max possible Manhattan distance
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if canReach(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo