"""
DFS traversal of a graph
Credit: https://courses.csail.mit.edu/6.006/fall11/rec/rec14.pdf
"""

class DFSResult:
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {}  # Edge classification for directed graph.
        self.order = []
        self.t = 0

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {v: [] for v in vertices}

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def itervertices(self):
        return self.vertices

    def neighbors(self, v):
        return self.adj[v]

def dfs(g):
    """
    Main DFS wrapper to ensure all vertices are visited even in 
    disconnected graphs.
    """
    # ------------------------------------------------------------------
    # DFS INSIGHT: Use recursion (or a stack) to explore as deep as 
    # possible along each branch before backtracking. Useful for 
    # topological sort, cycle detection, and strongly connected components.
    # ------------------------------------------------------------------
    results = DFSResult()
    for vertex in g.itervertices():
        if vertex not in results.parent:
            dfs_visit(g, vertex, results)
    return results

def dfs_visit(g, v, results, parent=None):
    """
    Recursive helper to visit a node and its descendants.
    """
    # Step 1: Record entrance into node 'v'
    results.parent[v] = parent
    results.t += 1
    results.start_time[v] = results.t
    
    # Optional: classify the edge used to reach this node
    if parent:
        results.edges[(parent, v)] = 'tree'
    
    # Step 2: Explore each neighbor 'n' of 'v'
    for n in g.neighbors(v):
        # Step 3: If neighbor not visited, recurse
        if n not in results.parent:
            dfs_visit(g, n, results, v)
        # Step 4: Else if neighbor is currently being visited, it's a back edge (cycle!)
        elif n not in results.finish_time:
            results.edges[(v, n)] = 'back'
        # Step 5: Classify other edge types for directed graphs
        elif results.start_time[v] < results.start_time[n]:
            results.edges[(v, n)] = 'forward'
        else:
            results.edges[(v, n)] = 'cross'
            
    # Step 6: Record exit from node 'v'
    results.t += 1
    results.finish_time[v] = results.t
    # Topological order: nodes finishing later come earlier in order
    results.order.append(v)

# ---- Quick verification ----
if __name__ == "__main__":
    v = [0, 1, 2, 3]
    g = Graph(v)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("DFS traversal:")
    result = dfs(g)
    print("Nodes visited in finish order:", result.order)
    print("Edge classifications:", result.edges)
