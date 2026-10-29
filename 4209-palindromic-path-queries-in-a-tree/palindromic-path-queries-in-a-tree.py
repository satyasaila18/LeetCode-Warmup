class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]
        

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        order = [0]

        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        for u in reversed(order):
            max_size = 0

            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]

                    if size[v] > max_size:
                        max_size = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n

        current_pos = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = current_pos
                current_pos += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        arr = [0] * n

        for u in range(n):
            arr[pos[u]] = 1 << (ord(s[u]) - ord('a'))

        size_tree = 1

        while size_tree < n:
            size_tree <<= 1

        seg = [0] * (2 * size_tree)

        for i in range(n):
            seg[size_tree + i] = arr[i]

        for i in range(size_tree - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(index, value):
            p = size_tree + index
            seg[p] = value

            p >>= 1

            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p >>= 1

        def range_xor(l, r):
            l += size_tree
            r += size_tree

            result = 0

            while l <= r:
                if l & 1:
                    result ^= seg[l]
                    l += 1

                if not (r & 1):
                    result ^= seg[r]
                    r -= 1

                l >>= 1
                r >>= 1

            return result

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])

            return result

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                update(pos[u], 1 << (ord(c) - ord('a')))

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)

                answer.append(
                    mask == 0 or (mask & (mask - 1)) == 0
                )

        return answer