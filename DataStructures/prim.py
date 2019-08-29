import queue

dic = {
    'a': [(8, 'b'), (5, 'c')],
    'b': [(8, 'a'), (10, 'c'), (2, 'd'), (18, 'e')],
    'c': [(5, 'a'), (10, 'b'), (3, 'd'), (16, 'f')],
    'd': [(2, 'b'), (3, 'c'), (12, 'e'), (30, 'f')],
    'e': [(18, 'b'), (12, 'd'), (4, 'g')],
    'f': [(16, 'c'), (30, 'd'), (26, 'g')],
    'g': [(4, 'e'), (14, 'd'), (26, 'f')],
}

def prim(dic):
    iter_lst, ans = [], []
    visited = set()
    start_point = next(iter(dic))
    q = queue.PriorityQueue()
    for edge in dic[start_point]:
        q.put((edge[0], edge[1], start_point))
    while len(visited) < len(dic):
        dis, v1, v2 = q.get()
        visited.add(v2)
        if not (v1 in visited and v2 in visited):
            ans.append((dis, v1, v2))
        for edge in dic[v1]:
            if not (edge[1] in visited and v1 in visited):
                q.put((edge[0], edge[1], v1))
    return ans


print(prim(dic))
