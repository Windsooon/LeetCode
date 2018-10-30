graph = {
    'A': ['B', 'C', 'X'],
    'B': ['D', 'E'],
    'D': ['E', 'P'],
    'P': ['X'],
    'X': ['C']}


def topsort(graph):
    visited = set()
    lst = []

    def dfs(element, visited, graph, lst):
        visited.add(element)
        try:
            graph[element]
        except KeyError:
            # lst = [0]
            lst.append(element)
            return
        # [0, 2]
        for g in graph[element]:
            if g not in visited:
                # visietd = {0, 5, 2, 3, 1}
                visited.add(g)
                dfs(g, visited, graph, lst)
        if element not in lst:
            lst.append(element)
    for k in graph.keys():
        dfs(k, visited, graph, lst)
    print(lst)


topsort(graph)
