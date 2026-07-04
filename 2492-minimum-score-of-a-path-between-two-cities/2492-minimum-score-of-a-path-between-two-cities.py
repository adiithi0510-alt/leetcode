from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))

        visited = [False] * (n + 1)
        visited[1] = True
        dq = deque([1])
        min_score = float('inf')

        while dq:
            u = dq.popleft()
            for v, d in adj[u]:
                min_score = min(min_score, d)
                if not visited[v]:
                    visited[v] = True
                    dq.append(v)

        return min_score
        