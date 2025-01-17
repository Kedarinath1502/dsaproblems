class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, weight=None):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

    def remove_edge(self, u, v):
        if u in self.graph:
            self.graph[u] = [pair for pair in self.graph[u] if pair[0] != v]
        if not self.directed and v in self.graph:
            self.graph[v] = [pair for pair in self.graph[v] if pair[0] != u]

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for u in self.graph:
            self.graph[u] = [pair for pair in self.graph[u] if pair[0] != vertex]

    def get_neighbors(self, vertex):
        return [pair[0] for pair in self.graph.get(vertex, [])]

    def has_edge(self, u, v):
        return any(pair[0] == v for pair in self.graph.get(u, []))

    def display(self):
        for vertex in self.graph:
            neighbors = ', '.join([str(neighbor[0]) for neighbor in self.graph[vertex]])
            print(f"{vertex}: {neighbors}")
