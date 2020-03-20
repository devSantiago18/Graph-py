# Graph with networkx
import networkx as nx
import matplotlib.pyplot as plt
import re

patron = re.compile('\(([a-zA-Z\d]),([a-zA-Z\d])\)')


graph = nx.Graph()
def create_graph(node,edge=()):
    plt.close()
    graph.add_node(node)
    if edge != () :
        graph.add_edge(*edge)
        nx.draw(graph)
        plt.show() # display

#print("Nodes of graph: ")
#print(graph.nodes())
#print("Edges of graph: ")
#print(graph.edges())

while True:
    node = input("Type de node : ")
    edge_input = input("Type de edge: ")
    if edge_input == "":
        create_graph(node)
    elif re.search(patron,edge_input) != None:
        create_graph(node,re.search(patron,edge_input).groups())
    else:
        print("Incorrect input")
        print("Edge: {}".format(re.search(patron,edge_input)))
        print("Node {}".format(node))

