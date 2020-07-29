# Graph with networkx
import networkx as nx
import matplotlib.pyplot as plt
import csv
from random import randrange


class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def __str__(self):
        return f"Nodes: {self.graph.nodes()}. Edges: {self.graph.edges()}."

    def create_nodes_from_file(self, path):
        with open(path, newline='') as file:
            reader = csv.reader(file, delimiter=' ')
            for row in reader:
                user, passw, _id, _next = row
                self.graph.add_edge(_id,_next)
                self.graph.add_node(_id)

    def draw(self, path=None):
        print(self.graph.nodes)
        nx.draw(self.graph)
        # Save as a png file
        # plt.savefig("simple_path.png")
        # Display
        plt.show()
