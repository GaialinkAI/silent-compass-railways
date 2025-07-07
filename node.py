# Silent Compass for Railways
# Decentralized Railway Navigation Without Internet or GPS
# Copyright (c) 2025 Ali Reza Farshad Fard
# GaiaLink Intelligence Systems Inc.
# Licensed under the MIT License

class Node:
    """Rail node with local field sensing & neighbor awareness."""
    def __init__(self, name, field_value):
        self.name = name
        self.field = field_value  # scalar gradient value
        self.neighbors = []       # filled by network

    def choose_next_hop(self):
        """Greedy descent: pick neighbor with lowest field."""
        if not self.neighbors:
            return None
        best = min(self.neighbors, key=lambda n: n.field)
        return best if best.field < self.field else None
