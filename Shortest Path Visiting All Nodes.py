import queue
class Solution:
    def shortestPathLength(self, graph):
        q = queue.Queue()
        count = 0
        state = []
        for i in range(len(graph)):
            q.put((i, set([i]), 0))
        state.append([0, set([0])])
        while not q.empty():
            current, visited, count = q.get()
            if len(visited) == len(graph):
                return count
            for g in graph[current]:
                tmp = visited.copy()
                tmp.add(g)
                if [g, tmp] not in state:
                    q.put((g, tmp, count+1))
        return -1

import collections
class Solution:
    def shortestPathLength(self, graph):
        breakpoint()
        memo = set()
        final = (1 << len(graph)) - 1
        q = collections.deque([(i, 0, 1 << i) for i in range(len(graph))])
        while q:
            node, steps, state = q.popleft()
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append((v, steps + 1, state | 1 << v))
                    memo.add((state | 1 << v, v))

s = Solution()
graph = [[1,5],[0,3],[3,5],[1,2,5],[7],[0,7,6,2,3],[5],[5,4,8],[7]]
print(s.shortestPathLength(graph))
