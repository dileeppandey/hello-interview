"""
BFS traversal of a graph
Credit: https://courses.csail.mit.edu/6.006/fall11/rec/rec13.pdf
"""
from collections import deque, OrderedDict

class BFSResult:
    def __init__(self):
        self.level = OrderedDict()
        self.parent = OrderedDict()

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

def bfs(g, s):
    """
    Queue based implementation of BFS
    @param g: a graph with adjacency list adj such that g.adj[u] us a list of 
    u's neighbors
    @param s: source
    """
    r = BFSResult()
    r.level[s] = 0
    r.parent[s] = None

    i = 1
    q = deque()
    q.append(s)

    while len(q) != 0:
        size = len(q)
        for i in range(size):
            u = q.popleft()
            for v in g.adj[u]:
                if v not in r.level:
                    r.level[v] = r.level[u] + 1
                    r.parent[v] = u
                    q.append(v)
    
    return r
