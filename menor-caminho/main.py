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

menor = vertices.shortest_path(10)
print(menor)


path = []
last_element = vertices.grafo[-1]

def menor_caminho_dinamico(grafo, inicio, fim):
    distancias = {inicio: 0}
    for i in range(len(grafo) - 1):
        for u, v, w in grafo:
            if u in distancias:
                if v not in distancias:
                    distancias[v] = distancias[u] + w
                else:
                    distancias[v] = min(distancias[v], distancias[u] + w)
    return distancias[fim]
