class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
            
        bus=defaultdict(set)
        q=deque([])
        visited_buses=set()
        visited_stops=set()

        for i in range(len(routes)):
            for stops in routes[i]:
                bus[stops].add(i)

        for b in bus[source]:
            q.append((b, 1))
            visited_buses.add(b)

        while q:
            node,cnt=q.popleft()

            for stops in routes[node]:
                if stops==target:
                    return cnt
                if stops in visited_stops:
                    continue
                visited_stops.add(stops)
                for b in bus[stops]:
                    if b not in visited_buses:
                        visited_buses.add(b)
                        q.append((b,cnt+1))

        return -1
