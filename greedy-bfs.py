import networkx as nx
import matplotlib.pyplot as plt
from classes.gbfs import BfsTraverser
# from classes.bfs import bfs

G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","STC","parkingLot","Phase3","J1","Mada"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes

G.add_edge("SportsComplex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph.1A",weight=10)
G.add_edge("Siwaka","Ph.1B",weight=230)
G.add_edge("Ph.1A","Mada",weight=850)
G.add_edge("Ph.1A","Ph.1B",weight=100)
G.add_edge("Ph.1B","Phase2",weight=112)
G.add_edge("Ph.1B","STC",weight=50)
G.add_edge("STC","Phase2",weight=50)
G.add_edge("STC","parkingLot",weight=250)
G.add_edge("Phase2","J1",weight=600)
G.add_edge("Phase2","Phase3",weight=500)
G.add_edge("Phase3","parkingLot",weight=350)
G.add_edge("J1","Mada",weight=200)
G.add_edge("parkingLot","Mada",weight=700)
# position the nodes to resemble map given
G.nodes["SportsComplex"]["pos"]=(-8,4)
G.nodes["Siwaka"]["pos"]=(-2,4)
G.nodes["Ph.1A"]["pos"]=(1,4)
G.nodes["Ph.1B"]["pos"]=(0,0)
G.nodes["Phase2"]["pos"]=(3,0)
G.nodes["STC"]["pos"]=(0,-2)
G.nodes["J1"]["pos"]=(6,0)
G.nodes["Phase3"]["pos"]=(5,-2)
G.nodes["parkingLot"]["pos"]=(5,-6)
G.nodes["Mada"]["pos"]=(10,0)

# store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
# call GBFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"SportsComplex","parkingLot",heuristics=0)
# routes = bfs("SportsComplex","parkingLot", G)

# print (routes.visited)
# route_list = routes.visited
print(route_bfs.visited)
route_list = route_bfs.visited

# color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
# color the adges as well
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]


arc_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G,node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G,node_pos,width=2,edge_color=edge_col)

nx.draw_networkx_edge_labels(G,node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()




