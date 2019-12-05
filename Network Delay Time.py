import collections
import heapq
from collections import defaultdict
from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times, N, K):
        distance = [0] + [float('inf')] * N
        graph = self.create_graph(times)
        result = self.dia(times, K, distance, graph)
        if result == float('inf'):
            return -1
        return result

    def create_graph(self, times):
        '''
        '''
        d = defaultdict(list)
        for t in times:
            d[t[0]].append((t[1], t[2]))
        return d

    def dia(self, times, source, distance, graph):
        '''
        '''
        # init queue()
        q = PriorityQueue()
        q.put((0, source))
        # calculate distance
        while not q.empty():
            dis, vertex = q.get()
            if dis <= distance[vertex]:
                distance[vertex] = dis
                for v in graph[vertex]:
                    if dis + v[1] < distance[v[0]]:
                        distance[v[0]] = dis + v[1]
                        q.put((distance[v[0]], v[0]))
        return max(distance)

class Solution:
    def networkDelayTime(self, times, N, K):
        t, graph, q = [0] + [float("inf")] * N, collections.defaultdict(list), collections.deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time <= t[node]:
                t[node] = time
                for v, w in graph[node]:
                    if t[v] > time + w:
                        t[v] = time + w
                        q.append((t[v], v))
        mx = max(t)
        return mx if mx < float("inf") else -1

s = Solution()
N = 3
K = 2
times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
breakpoint()
print(s.networkDelayTime(times, N, K))
