import collections
import queue

class Solution:
    def shortestSuperstring(self, A):
        lst = self.build_graph(A)
        return self.prim(lst, A)

    def calculate_distance(self, str1, str2):
        first = second = 0
        for i in range(len(str2)):
            if str1.startswith(str2[i:]):
                first = len(str2) - i
        for i in range(len(str1)):
            if str2.startswith(str1[i:]):
                second = len(str1) - i
        return -second, -first

    def build_graph(self, A):
        dic = collections.defaultdict(list)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                first, second = self.calculate_distance(A[i], A[j])
                dic[A[i]].append((first, A[i], A[j]))
                dic[A[j]].append((second, A[j], A[i]))
        return dic

    # def Borůvka(self, dic, A):
    #     graph = []
    #     safe_edges = [(0, 0), 0] * len(A)
    #     for k in dic:
    #         for l in k:
    #             if safe_edges[k] == 0 or l[1] > safe_edges[k][1]:
    #                 safe_edges[k] = [(k, l[0]), l[1]]
    #     for s in safe_edges:
    #         graph.append(s)
    def prim(self, lst, A):
        qu = queue.PriorityQueue()
        ans = []
        visited = set()
        qu.put(lst[next(iter(lst))])
        while len(visited) < len(A):
            vertex_lst = []
            while not qu.empty():
                vertex_lst.append(qu.get())
            tem_qu = queue.PriorityQueue()
            for vertex in vertex_lst:
                for v in vertex:
                    tem_qu.put(v)
            while not tem_qu.empty():
                edges = tem_qu.get()
                if not (edges[1] in visited and edges[2] in visited):
                    ans.append(edges)
                    break
            visited.add(edges[1])
            visited.add(edges[2])
            for v in visited:
                qu.put(lst[v])
                qu.put(lst[v])
        return ans



s = Solution()
A = ["catg","ctaagt","gcta","ttca","atgcatc"]
# A = ["catg", "ctaagt", "gcta"]
print(s.shortestSuperstring(A))
