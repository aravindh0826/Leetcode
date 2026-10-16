class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, l, r):
            if lazy[node]:
                v = lazy[node]
                length = r - l + 1

                sq[node] = (sq[node] + 2 * v * tree[node]
                            + v * v * length) % MOD
                tree[node] = (tree[node] + v * length) % MOD

                if l != r:
                    lazy[node * 2] += v
                    lazy[node * 2 + 1] += v

                lazy[node] = 0

        def update(node, l, r, ql, qr):
            push(node, l, r)

            if r < ql or l > qr:
                return

            if ql <= l and r <= qr:
                lazy[node] += 1
                push(node, l, r)
                return

            mid = (l + r) // 2
            update(node * 2, l, mid, ql, qr)
            update(node * 2 + 1, mid + 1, r, ql, qr)

            tree[node] = (tree[node * 2]
                          + tree[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2]
                        + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans
        