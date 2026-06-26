class Solution {

    class FenwickTree {
        long[] bit;
        int n;

        FenwickTree(int n) {
            this.n = n;
            bit = new long[n + 1];
        }

        void update(int idx, long val) {
            while (idx <= n) {
                bit[idx] += val;
                idx += idx & -idx;
            }
        }

        long query(int idx) {
            long sum = 0;
            while (idx > 0) {
                sum += bit[idx];
                idx -= idx & -idx;
            }
            return sum;
        }
    }

    public long countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;

        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + (nums[i] == target ? 1 : -1);
        }

        long[] values = prefix.clone();
        Arrays.sort(values);

        ArrayList<Long> unique = new ArrayList<>();
        for (long v : values) {
            if (unique.isEmpty() || unique.get(unique.size() - 1) != v) {
                unique.add(v);
            }
        }

        FenwickTree ft = new FenwickTree(unique.size());

        long ans = 0;

        for (long p : prefix) {
            int rank = lowerBound(unique, p) + 1;
            ans += ft.query(rank - 1);
            ft.update(rank, 1);
        }

        return ans;
    }

    private int lowerBound(ArrayList<Long> list, long target) {
        int l = 0, r = list.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (list.get(m) < target)
                l = m + 1;
            else
                r = m;
        }
        return l;
    }
}