# Silent Compass for Railways
# Decentralized Railway Navigation Without Internet or GPS
# Copyright (c) 2025 Ali Reza Farshad Fard
# GaiaLink Intelligence Systems Inc.
# Licensed under the MIT License

import json, random, os, networkx as nx, matplotlib.pyplot as plt
from node import Node

# --- locate data file relative to script ---
base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, 'rail_network.json')) as f:
    data = json.load(f)

# --- build graph ---
G = nx.Graph()
nodes = {name: Node(name, val) for name, val in data['field'].items()}
for u, v in data['edges']:
    G.add_edge(u, v)
    nodes[u].neighbors.append(nodes[v])
    nodes[v].neighbors.append(nodes[u])

# --- random start & greedy descent ---
start = random.choice(list(nodes.values()))
global_min = min(nodes.values(), key=lambda n: n.field)
path = [start]
current = start
while True:
    nxt = current.choose_next_hop()
    if nxt is None:
        break
    path.append(nxt)
    current = nxt

# --- console output ---
print(f"Start node: {start.name} (field={start.field})")
print(f"Arrived at: {current.name} (field={current.field})")
print("Path taken:", [n.name for n in path])
print(f"Global minimum: {global_min.name} (field={global_min.field})")

# --- plot ---
pos = {name: tuple(map(int, name.strip('()').split(', '))) for name in nodes}
nx.draw(G, pos, with_labels=False, node_size=200)
xs, ys = zip(*[pos[n.name] for n in path])
plt.plot(xs, ys, linewidth=3)
plt.title('Silent Compass Path')
plt.show()
