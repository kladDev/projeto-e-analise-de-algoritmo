class Grafo:

    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.grafo = [[] for _ in range(self.vertices)]

    def shortest_path(self, start):
        path = {}
        path[start] = 0

        for _ in range(self.vertices - 1):
            for vertex in range(1, self.vertices + 1):
                if vertex not in path:
                    continue

                for neighbor, weight in self.grafo[vertex - 1]:
                    if (neighbor not in path) or (path[vertex] + weight < path[neighbor]):
                        path[neighbor] = path[vertex] + weight

        return path

    def add_edge(self, element1, element2, weight):
        self.grafo[element1-1].append([element2, weight])
        self.grafo[element2-1].append([element1, weight])