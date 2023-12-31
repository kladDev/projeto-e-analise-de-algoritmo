from grafo import Grafo

vertices = Grafo(10)
vertices.add_edge(1, 2, 9)
vertices.add_edge(1, 4, 7)
vertices.add_edge(1, 3, 6)
vertices.add_edge(2, 5, 3)
vertices.add_edge(2, 6, 5)
vertices.add_edge(3, 7, 3)
vertices.add_edge(4, 5, 2)
vertices.add_edge(4, 6, 4)
vertices.add_edge(4, 7, 6)
vertices.add_edge(5, 8, 5)
vertices.add_edge(5, 9, 3)
vertices.add_edge(6, 8, 7)
vertices.add_edge(7, 9, 7)
vertices.add_edge(8, 10, 4)
vertices.add_edge(9, 10, 9)

print(vertices.grafo)
path = vertices.shortest_path(10)
print(path)