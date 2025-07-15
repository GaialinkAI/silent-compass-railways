import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import json

# Load your rail network
with open("rail_network.json") as f:
    rail_data = json.load(f)

# Create a graph
G = nx.Graph()
for node in rail_data["nodes"]:
    G.add_node(node["id"], label=node["label"])

for edge in rail_data["edges"]:
    G.add_edge(edge["source"], edge["target"])

# Streamlit UI
st.title("Silent Compass Railway Navigation (Demo)")
st.write("Decentralized railway route planner without GPS or Internet.")

# Plot the graph
fig, ax = plt.subplots()
nx.draw(G, with_labels=True, ax=ax, node_color="skyblue", node_size=800)
st.pyplot(fig)
