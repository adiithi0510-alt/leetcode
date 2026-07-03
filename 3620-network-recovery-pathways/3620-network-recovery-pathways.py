from collections import defaultdict, deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        # 1. Drop edges touching offline nodes (0 and n-1 are always online)
        filtered = [(u, v, c) for u, v, c in edges if online[u] and online[v]]
        if not filtered:
            return -1

        adj = defaultdict(list)
        indeg = [0] * n
        for u, v, c in filtered:
            adj[u].append((v, c))
            indeg[v] += 1

        # 2. One topological order (valid for any cost-subset of these edges)
        order = []
        dq = deque(i for i in range(n) if indeg[i] == 0)
        indeg_work = indeg[:]
        while dq:
            u = dq.popleft()
            order.append(u)
            for v, c in adj[u]:
                indeg_work[v] -= 1
                if indeg_work[v] == 0:
                    dq.append(v)

        costs = sorted(set(c for _, _, c in filtered))

        def feasible(X):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0
            for u in order:
                if dist[u] == INF:
                    continue
                du = dist[u]
                for v, c in adj[u]:
                    if c >= X and du + c < dist[v]:
                        dist[v] = du + c
            return dist[n - 1] <= k

        # 3. Binary search for the largest feasible score
        lo, hi, ans = 0, len(costs) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans