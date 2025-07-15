import streamlit as st
import json
import networkx as nx
import matplotlib.pyplot as plt

# Title
st.title("🚄 Silent Compass Railway Simulator")

# Load rail network data
with open("rail_network.json") as f:
    rail_data = json.load(f)

# Initialize the graph
G = nx.Graph()

# Add nodes from the 'field' dict
for node_str, value in rail_data["field"].items():
    node = eval(node_str)  # convert string like "(0, 0)" to tuple
    G.add_node(node, value=value)

# Add edges from the 'edges' list
for edge in rail_data["edges"]:
    node1 = eval(edge[0])
    node2 = eval(edge[1])
    G.add_edge(node1, node2)

# Draw the graph
fig, ax = plt.subplots(figsize=(8, 8))
pos = {node: node for node in G.nodes()}  # use coordinates as positions
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=600, ax=ax)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): "" for u, v in G.edges()}, ax=ax)
ax.set_title("Decentralized Rail Network")
st.pyplot(fig)

# Optional: Display raw data
with st.expander("📦 Show Raw Data"):
    st.json(rail_data)

