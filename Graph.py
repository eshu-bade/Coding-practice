"""
This program is to check the paths between cities and shortest path between them using a Graph.
Graph is a non-linear data structure. It is similar to Tree.

All Trees are Graphs but all Graphs are not Trees.
Types of Graphs:
Simple Path: All nodes are distinct Ex: (A,B,C,D,E)
Closed Path: If path starts and ends with the same Node, it forms a circular path. The nodes can be repeated Ex: (C, E, A, E, G, C)

Connected Graph: If we can reach from one node to another node, it is said to be Connected Graph.
Cycle: It is a path in which first and last node of the path is same and all the other nodes are distinct.
"""


class Graph:
    def __init__(self, edges):
        self.edges = edges
        # Creating a dictionary using tuples
        self.graphDictionary = {}
        for start, end in self.edges:
            if start in self.graphDictionary:
                self.graphDictionary[start].append(end)
            else:
                self.graphDictionary[start] = [end]
        print("Graph dictionary is: ", self.graphDictionary)

    def getAllPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDictionary:
            return None
        paths = []
        for node in self.graphDictionary[start]:
            if node not in path:
                newPaths = self.getAllPaths(node, end, path)
                for p in newPaths:
                    paths.append(p)
        return paths

    def getShortestPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        if start not in self.graphDictionary:
            return None
        shortestPath = None

        for node in self.graphDictionary[start]:
            if node not in path:
                sp = self.getShortestPath(node, end, path)
                if sp:
                    if shortestPath is None or len(sp) < len(shortestPath):
                        shortestPath = sp

        return shortestPath


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    routes0 = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
    routeGraph = Graph(routes)
    start = "Mumbai"
    end = "New York"
    print(routeGraph.getAllPaths(start, end))
    print(f"Shortest path between {start} and {end}: ", routeGraph.getShortestPath(start, end))
