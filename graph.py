# Graph with networkx
import networkx as nx
import matplotlib.pyplot as plt
import random




def create_graph():
    graph = nx.Graph()
    # read file, create nodes 
    nodes = []
    file = open('nodes.txt','r')
    for line in file.readlines():
        if line != "": 
            nodes.append(line.replace("\n",""))
    file.close()

    graph.add_nodes_from(nodes)

    num_random = []
    for i in range(len(nodes)):
        """ 
        if i < len(nodes)-1:
            edge = (nodes[i],nodes[i+1])
            graph.add_edge(*edge)
        """     
        ran = random.randrange(len(nodes))
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