class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
        
        for a, b in edges:
            union(a, b)
        
        vertex_count = {}
        edge_count = {}
        for i in range(n):
            r = find(i)
            vertex_count[r] = vertex_count.get(r, 0) + 1
            edge_count.setdefault(r, 0)
        
        for a, b in edges:
            r = find(a)
            edge_count[r] += 1
        
        result = 0
        for r in vertex_count:
            v = vertex_count[r]
            e = edge_count[r]
            if e == v * (v - 1) // 2:
                result += 1
        
        return result
        