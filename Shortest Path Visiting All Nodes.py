class Solution:
    def shortestPathLength(self, graph):
        memo, final, q, steps = set(), (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))], 0
        breakpoint()
        while True:
            new = []
            for node, state in q:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            q = new
            steps += 1


s = Solution()
graph = [[1],[0,2],[1,3,4],[2], [2]]
print(s.shortestPathLength(graph))
