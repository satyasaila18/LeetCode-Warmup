
import heapq
from sortedcontainers import SortedSet

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        busy = []
        avail_set = SortedSet(range(k))
        requests_handled = [0] * k

        for i, (arr_time, proc_load) in enumerate(zip(arrival, load)):

            # Release servers whose requests are completed
            while busy and busy[0][0] <= arr_time:
                _, freed_server = heapq.heappop(busy)
                avail_set.add(freed_server)

            # No server available
            if not avail_set:
                continue

            # Preferred server
            target = i % k

            # Find the next available server
            idx = avail_set.bisect_left(target)

            if idx == len(avail_set):
                idx = 0

            server_id = avail_set[idx]
            avail_set.remove(server_id)

            # Mark server as busy
            heapq.heappush(busy, (arr_time + proc_load, server_id))

            requests_handled[server_id] += 1

        max_handled = max(requests_handled)

        return [
            sid for sid, count in enumerate(requests_handled)
            if count == max_handled
        ]
