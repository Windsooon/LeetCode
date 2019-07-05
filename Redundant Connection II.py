class Solution:
    def findRedundantDirectedConnection(self, edges):
        '''
        return the redundant edge from edges

        case 1 if there is a loop:
          if we found node with two parents
               return the parent edge occure in the loop
          else:
               return current edge
        case 2 there is no loop:
          return the second edge from the node with two parents

        input: graph
        output: redundant edge
        '''
        self.edges = edges
        self.aedge = None
        candidates = self.get_candidates()
        path = self.circle_path(candidates)

        # case 1
        if path:
            return path
        # case 2
        else:
            return candidates[-1]


    def circle_path(self, candidates):
        """
        check if the graph has loop, if it has, return the loop path
        else return None

        output:
            if the graph has circle:
                if candidates:
                    return the circle path
                else:
                    return the last occur edge in the loop
            else:
                return None
        """
        path = []
        visited = {}

        def visit(edge):
            if edge[0] in visited:
                return
            path.append(edge[0])
            visited[edge[0]] = True
            for e in self.edges:
                if e[0] == edge[1]:
                    if e[1] in path:
                        path.append(e[0])
                        path.append(e[1])
                        ans = self.get_edge(e, path, candidates)
                        return ans
                    ans = visit(e)
                    if ans:
                        return ans
            path.pop()
            return False

        for e in self.edges:
            tem_path = visit(e)
            if tem_path:
                return tem_path
        return

    def get_edge(self, edge, path, candidates):
        if candidates:
            tem_path = path[path.index(path[-1]):]
            real_path = self.get_real_path(tem_path)
            for can in candidates:
                if can in real_path:
                    return can
        else:
            return edge

    def get_real_path(self, path):
        '''
        return lst base path from path
        >>> get_real_path([1,2,3,1])
        >>> [[1,2],[2,3],[3,1]]
        '''
        lst = []
        # [1,2,3,1] -> [[1,2],[2,3],[3,1]]
        for i in range(len(path)-1):
            lst.append(path[i:i+2])
        return lst



    def get_candidates(self):
        """
        return the edge points to the same node,
        return empty lst we we can't find any

        input:
        output: list
        """
        visited = {}
        for e in self.edges:
            if e[1] in visited:
                visited[e[1]].append(e)
                return visited[e[1]]
            else:
                visited[e[1]] = []
                visited[e[1]].append(e)
        return []



s = Solution()
assert (s.findRedundantDirectedConnection([[1,2], [1,3], [2,3]])) == [2, 3]
assert s.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]) == [4, 1]
assert s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]) == [2, 1]
assert (s.findRedundantDirectedConnection([[4,1],[1,5],[4,2],[5,1],[4,3]])) == [5, 1]
