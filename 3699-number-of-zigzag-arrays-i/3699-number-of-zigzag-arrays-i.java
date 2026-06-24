class Solution {
    private static final long MOD = 1_000_000_007L;

    public int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;

        long[] up = new long[m + 1];
        long[] down = new long[m + 1];

        // Length = 2
        for (int v = 1; v <= m; v++) {
            up[v] = v - 1;      // previous value is smaller
            down[v] = m - v;    // previous value is larger
        }

        // Build lengths 3..n
        for (int len = 3; len <= n; len++) {
            long[] prefUp = new long[m + 1];
            long[] prefDown = new long[m + 1];

            for (int v = 1; v <= m; v++) {
                prefUp[v] = (prefUp[v - 1] + up[v]) % MOD;
                prefDown[v] = (prefDown[v - 1] + down[v]) % MOD;
            }

            long totalUp = prefUp[m];

            long[] newUp = new long[m + 1];
            long[] newDown = new long[m + 1];

            for (int v = 1; v <= m; v++) {
                // Last comparison is up, so previous one must be down
                newUp[v] = prefDown[v - 1];

                // Last comparison is down, so previous one must be up
                newDown[v] = (totalUp - prefUp[v] + MOD) % MOD;
            }

            up = newUp;
            down = newDown;
        }

        long ans = 0;
        for (int v = 1; v <= m; v++) {
            ans = (ans + up[v] + down[v]) % MOD;
        }

        return (int) ans;
    }
}