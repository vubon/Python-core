import networkx as nx
G=nx.Graph()
G.add_node("A")
G.add_node("B")
G.add_none("C")
G.add_edge("A","B")
G.add_edge("B", "C")
G.add_edge("C", "A")

print("Nodes: " + str(G.nodes()))
print("Edges: " + str(G.edge()))
