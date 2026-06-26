import java.util.*;

class Solution {

    class State {
        int x, y, used;
        long cost;

        State(int x, int y, int used, long cost) {
            this.x = x;
            this.y = y;
            this.used = used;
            this.cost = cost;
        }
    }

    class Cell {
        int val, x, y;

        Cell(int val, int x, int y) {
            this.val = val;
            this.x = x;
            this.y = y;
        }
    }

    class Fenwick {
        int[] bit;
        int n;

        Fenwick(int n) {
            this.n = n;
            bit = new int[n + 2];
        }

        void update(int idx, int val) {
            while (idx <= n) {
                bit[idx] += val;
                idx += idx & -idx;
            }
        }

        int query(int idx) {
            int sum = 0;
            while (idx > 0) {
                sum += bit[idx];
                idx -= idx & -idx;
            }
            return sum;
        }
    }

    public int minCost(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int total = m * n;

        Cell[] cells = new Cell[total];
        int idx = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cells[idx++] = new Cell(grid[i][j], i, j);
            }
        }

        Arrays.sort(cells, Comparator.comparingInt(a -> a.val));

        long INF = Long.MAX_VALUE / 4;

        long[][][] dist = new long[m][n][k + 1];

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                Arrays.fill(dist[i][j], INF);

        dist[0][0][0] = 0;

        PriorityQueue<State> pq = new PriorityQueue<>((a, b) -> Long.compare(a.cost, b.cost));
        pq.offer(new State(0, 0, 0, 0));

        int[] processed = new int[k + 1];
        Arrays.fill(processed, -1);

        while (!pq.isEmpty()) {

            State cur = pq.poll();

            if (cur.cost != dist[cur.x][cur.y][cur.used])
                continue;

            if (cur.x == m - 1 && cur.y == n - 1)
                return (int) cur.cost;

            // Move Down
            if (cur.x + 1 < m) {
                long nc = cur.cost + grid[cur.x + 1][cur.y];
                if (nc < dist[cur.x + 1][cur.y][cur.used]) {
                    dist[cur.x + 1][cur.y][cur.used] = nc;
                    pq.offer(new State(cur.x + 1, cur.y, cur.used, nc));
                }
            }

            // Move Right
            if (cur.y + 1 < n) {
                long nc = cur.cost + grid[cur.x][cur.y + 1];
                if (nc < dist[cur.x][cur.y + 1][cur.used]) {
                    dist[cur.x][cur.y + 1][cur.used] = nc;
                    pq.offer(new State(cur.x, cur.y + 1, cur.used, nc));
                }
            }

            // Teleport
            if (cur.used < k) {

                int lo = 0, hi = total;

                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (cells[mid].val <= grid[cur.x][cur.y])
                        lo = mid + 1;
                    else
                        hi = mid;
                }

                int limit = lo - 1;

                while (processed[cur.used] < limit) {

                    processed[cur.used]++;

                    Cell c = cells[processed[cur.used]];

                    if (cur.cost < dist[c.x][c.y][cur.used + 1]) {
                        dist[c.x][c.y][cur.used + 1] = cur.cost;
                        pq.offer(new State(c.x, c.y, cur.used + 1, cur.cost));
                    }
                }
            }
        }

        return -1;
    }
}