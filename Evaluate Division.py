import collections
import queue
class Solution:
    def calcEquation(self, equations, values, queries):
        # {a: [(b, 2.0)]
        #  b: [(a, 1/2), (c, 3.0)]
        #  c: [(b, 1/3)]
        if not equations:
            return
        graph, showed = self.create_graph(equations, values)
        return self.calculate(queries, showed, graph)

    def create_graph(self, equations, values):
        '''
        create graph (dict object)
        depend on equations and values
        '''
        showed = set()
        dic = collections.defaultdict(list)
        for i in range(len(equations)):
            showed.add(equations[i][0])
            showed.add(equations[i][1])
            dic[equations[i][0]].append((equations[i][1], values[i]))
            dic[equations[i][1]].append((equations[i][0], 1/values[i]))
        return dic, showed

    def calculate(self, queries, showed, graph):
        '''
        Calculate the answer from every query
        '''
        ans = []
        for q in queries:
            ans.append(self.bfs(q, showed, graph))
        return ans

    def bfs(self, q, showed, graph):
        '''
        Search q[1] from q[0] in the graph and
        keep track of the val
        '''
        if q[0] not in showed or q[1] not in showed:
            return -1.0
        elif q[0] == q[1]:
            return 1.0
        visited = set()
        qu = queue.Queue()
        qu.put((q[0], 1))
        while not qu.empty():
            top, val = qu.get()
            if top == q[1]:
                return val
            visited.add(top)
            for node, multiply in graph[top]:
                if node not in visited:
                    qu.put((node, val*multiply))
        return -1

s = Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(s.calcEquation(equations, values, queries))
