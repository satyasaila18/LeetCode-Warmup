class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        pos = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick trees for counts and sums
        count = [0] * (m + 1)
        sums = [0] * (m + 1)

        def update(bit, i, val):
            while i <= m:
                bit[i] += val
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        # Find kth smallest element
        def kth(tree, k):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= m and tree[nxt] < k:
                    idx = nxt
                    k -= tree[nxt]

                step >>= 1

            return idx + 1

        # Calculate cost of current window
        def get_cost(total):
            mid = kth(count, (x + 1) // 2)
            median = vals[mid - 1]

            left_count = query(count, mid)
            left_sum = query(sums, mid)

            right_count = x - left_count
            right_sum = total - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        # Sliding window
        costs = []
        total = 0

        for i in range(x):
            v = nums[i]
            p = pos[v]

            update(count, p, 1)
            update(sums, p, v)
            total += v

        costs.append(get_cost(total))

        for i in range(x, n):

            # Remove outgoing element
            old = nums[i - x]
            p = pos[old]

            update(count, p, -1)
            update(sums, p, -old)
            total -= old

            # Add incoming element
            new = nums[i]
            p = pos[new]

            update(count, p, 1)
            update(sums, p, new)
            total += new

            costs.append(get_cost(total))

        # Dynamic Programming
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Skip current element
                curr[i] = curr[i - 1]

                # Select window ending at i-1
                if i >= x and prev[i - x] != INF:

                    val = prev[i - x] + costs[i - x]

                    curr[i] = min(curr[i], val)

            prev = curr

        return prev[n]