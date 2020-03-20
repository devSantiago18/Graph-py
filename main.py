# Graph with networkx
import networkx as nx
import matplotlib.pyplot as plt

# create an graph
graph = nx.Graph()
#print(graph.nodes()) # print nodes
#print(graph.edges()) # print edges

# adding just one node
graph.add_node('a')
#adding a list of nodes
graph.add_nodes_from(['b','c'])

#edges
graph.add_edge(1,2)

edge = ('d','e')
graph.add_edge(*edge)

edge = ('a','b')
graph.add_edge(*edge)

graph.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])



print("Nodes of graph: ")
print(graph.nodes())
print("Edges of graph: ")
print(graph.edges())

nx.draw(graph)
plt.savefig("simple_path.png") # save as png
plt.show() # display



