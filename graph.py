# Graph with networkx
import networkx as nx
import matplotlib.pyplot as plt
from random import randrange


class Graph:
    def __init__(self):
        self.graph = nx.Graph()
        self.nodes = []

    def __str__(self):
        return f"Nodes: {self.graph.nodes()}. Edges: {self.graph.edges()}."

    def create_nodes_from_file(self, path):
        with open(path, 'r') as file:
            for line in file.readlines():
                if line != "":
                    self.nodes.append(line.replace("\n", ""))
        self.graph.add_nodes_from(self.nodes)

    def generate_edges(self):
        generated = []
        for i in range(len(self.nodes)):
            index = randrange(len(self.nodes))
            if index not in generated:
                generated.append(index)
                edge = (self.nodes[i], self.nodes[index])
                self.graph.add_edge(*edge)

    def draw(self, path=None):
        nx.draw(self.graph)
        # Save as a png file
        # plt.savefig("simple_path.png")
        # Display
        plt.show()
