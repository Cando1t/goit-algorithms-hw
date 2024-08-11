import networkx as nx

#---directed graph---
G = nx.DiGraph(directed=True)

# add nodes
G.add_node('Singapore')
G.add_node('San Francisco')
G.add_node('Tokyo')
G.add_nodes_from(['Riga', 'Copenhagen'])

# add edges
G.add_edge('Singapore','San Francisco', weight=13574)
G.add_edge('San Francisco','Tokyo', weight=8269)
G.add_edge('Riga','Copenhagen', weight=868)
G.add_edge('Copenhagen','Singapore', weight = 9956)
G.add_edge('Singapore','Tokyo', weight = 5308)
G.add_edge('Riga','San Francisco', weight=9016)
G.add_edge('San Francisco','Singapore', weight=13574)
G.add_edge('Copenhagen','Riga', weight = 868)
G.add_edge('Singapore', 'Copenhagen', weight = 9956)
G.add_edge('Tokyo', 'Singapore', weight = 5308)
G.add_edge('Tokyo', 'San Francisco', weight=8269)

# set layout
pos = nx.circular_layout(G)

# draw graph
nx.draw(G, pos, with_labels = True)

# draw edge labels
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={
        ("Singapore","Tokyo"): '2 flights daily', 
        ("San Francisco","Singapore"): '5 flights daily',
    },
    font_color='red'
)


num_nodes = G.number_of_nodes() 
num_edges = G.number_of_edges() 
#is_connected = nx.is_connected(G)  
print('кількість вузлів:', num_nodes, ', кількість ребер:', num_edges)
print(G.degree)