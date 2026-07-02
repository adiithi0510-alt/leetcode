from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # health left when standing on (0,0), accounting for it being unsafe
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False
        
        best = [[-1] * n for _ in range(m)]
        best[0][0] = start_health
        
        q = deque([(0, 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c = q.popleft()
            h = best[r][c]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nh = h - grid[nr][nc]
                    if nh > 0 and nh > best[nr][nc]:
                        best[nr][nc] = nh
                        q.append((nr, nc))
        
        return best[m - 1][n - 1] >= 1