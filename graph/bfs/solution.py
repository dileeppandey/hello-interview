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
    
    @param g: a graph with adjacency list adj such that g.adj[u] is a list of 
    u's neighbors
    @param s: source node
    """
    # ------------------------------------------------------------------
    # BFS INSIGHT: Use a FIFO queue to visit nodes level-by-level.
    # This ensures that when we first reach a node, we've found the 
    # shortest path to it in an unweighted graph.
    # ------------------------------------------------------------------
    
    # Step 1: Initialize results and the starting node
    r = BFSResult()
    r.level[s] = 0
    r.parent[s] = None

    # Step 2: Initialize queue with the source node
    q = deque()
    q.append(s)

    # Step 3: Process the queue until it's empty
    while q:
        # Step 4: Dequeue the next node to explore
        u = q.popleft()
        
        # Step 5: For each neighbor 'v' of 'u'
        if u in g.adj:
            for v in g.adj[u]:
                # Step 6: If 'v' hasn't been visited yet (not in r.level)
                if v not in r.level:
                    # Step 7: Record its level and parent
                    r.level[v] = r.level[u] + 1
                    r.parent[v] = u
                    # Step 8: Enqueue 'v' to visit its neighbors later
                    q.append(v)
    
    return r

# ---- Quick verification ----
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("BFS starting from node 2:")
    result = bfs(g, 2)
    for node in result.level:
        print(f"Node: {node}, Level: {result.level[node]}, Parent: {result.parent[node]}")
