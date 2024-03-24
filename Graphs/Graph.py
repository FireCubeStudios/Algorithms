from Edge import Edge
import queue

# The graph has an array of all vertices with each array containing an array of all edges to other vertices
class Graph:
    def __init__(self, vertices):
        self.vertices = [[] for _ in range(vertices)]
        
    # Add an item to the undirected graph
    def add(self, origin, destination, isConflictEdge):
        self.vertices[origin].append(Edge(destination, isConflictEdge))
        self.vertices[destination].append(Edge(origin, isConflictEdge))
        return 
    
    # Return all adjacent vertices to the vertex
    def adjacent(self, vertex):
        return self.vertices[vertex]

    # Returns true if the graph is harmoniously 2 coloured
    def isHarmonious(self) -> bool:    
        q = queue.Queue(maxsize = 0)
        coloured = set()
        marked = set()
        q.put(0)
        while(not(q.empty())):
            origin = q.get()
            marked.add(origin)
            for edge in self.adjacent(origin):
                if(not(edge.value in marked)): # Was not previously visited so add to queue
                    q.put(edge.value)

                if(edge.value in marked): # Node has been visited
                    if(edge.isConflict): # Check if node is opposite colour 
                        if((origin in coloured and edge.value in coloured) or 
                        (not(origin in coloured) and not(edge.value in coloured))):
                            return False # Node is not opposite colour
                    else: # Check if node is same colour
                        if ((origin in coloured and not(edge.value in coloured)) 
                            or (not(origin in coloured) and edge.value in coloured)):
                            return False # Node is not same colour
                else: # Node has not been visited
                    marked.add(edge.value)
                    if(edge.isConflict):
                        if(not(origin in coloured)):
                            coloured.add(edge.value)
                    else:
                        if(origin in coloured):
                            coloured.add(edge.value)
            marked.add(origin)
        return True 