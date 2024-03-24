from Graph import Graph

vertices, edges = map(int, input().split())
graph = Graph(vertices)
for _ in range(edges):
    vertex1, vertex2, isConflictEdge = map(int, input().split())
    graph.add(vertex1, vertex2, (isConflictEdge == 1))
print(1 if(graph.isHarmonious()) else 0)
