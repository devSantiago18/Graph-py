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
        with open(path,'r') as file:
            for line in file.readlines():
                if line != "": 
                    self.nodes.append(line.replace("\n", ""))
        self.graph.add_nodes_from(self.nodes)
    
    def generate_edges(self):
        random_numbers = list()
        i = 0
        while i < len(self.nodes):
            num = randrange(len(nodes))
            if ran not in random_numbers:
                random_numbers.append(num)
                edge = (self.nodes[i], self.nodes[ran])
                self.graph.add_edge(*edge)
                i = i + 1
    
    def draw(self, path = None):
        nx.draw(self.graph)
        # Save as a png file
        #plt.savefig("simple_path.png")
        # Display
        plt.show()

def create_graph():
    graph = nx.Graph()
    # read file, create nodes 
    nodes = []
    with open('nodes.txt','r') as file:
        for line in file.readlines():
            if line != "": 
                nodes.append(line.replace("\n",""))
    graph.add_nodes_from(nodes)

    num_random = []
    for i in range(len(nodes)):
        """ 
        if i < len(nodes)-1:
            edge = (nodes[i],nodes[i+1])
            graph.add_edge(*edge)
        """     
        ran = randrange(len(nodes))
        if ran not in num_random:
            num_random.append(ran)
            edge = (nodes[i],nodes[ran])
            graph.add_edge(*edge)
        
    print("Nodes of graph: ")
    print(graph.nodes())
    print("Edges of graph: ")
    print(graph.edges())

    nx.draw(graph)
    #plt.savefig("simple_path.png") # save as png
    plt.show() # display
