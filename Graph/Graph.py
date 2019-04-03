class Vertex(object):
    def __init__(self, val, connected_to):

        self.val = val
        self.connected_to = connected_to


class Edge(object):
    def __init__(self, connected_from, connected_to, val):
        self.connected_from = connected_from
        self.connected_to = connected_to
        self.val = val


class Graph(object):
    def __init__(self):
        pass
