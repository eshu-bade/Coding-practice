""""
            A
        /   |   \    - Edges
       B    C    D     Vertices
     /  \      /   \
    E    F    G     H
       /  \   \
     I     J   K


Output array: [A,B,E,F,I,J,C,D,G,K,H]

Time complexity O(V+E), Space O(V)
V = vertices, E = Edges
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
