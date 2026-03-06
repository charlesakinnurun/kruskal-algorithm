import matplotlib.pyplot as plt
import networkx as nx

class DisjointSetUnion:
    """
    Disjoint Set Union (DSU) or Union-Find data structure.
    Used to keep track of connected components and detect cycles in Kruskal's algorithm.
    """
    def __init__(self, nodes):
        # Initialize parent pointers: each node is its own parent (its own set)
        self.parent = {node: node for node in nodes}
        # Rank is used to keep the tree flat during unions (Union by Rank)
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        """Find the root of the set containing 'node' with Path Compression."""
        if self.parent[node] != node:
            # Recursively find the root and compress the path by pointing
            # the node directly to the root.
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        """Unite the sets containing 'u' and 'v'."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank: attach the smaller tree under the root of the larger tree
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                # If ranks are equal, pick one and increment its rank
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False # u and v were already in the same set (cycle detected)

def kruskal_algorithm(nodes, edges):
    """
    Kruskal's Algorithm to find the Minimum Spanning Tree (MST).
    
    Args:
        nodes: List of node names (e.g., ['A', 'B', 'C'])
        edges: List of tuples (u, v, weight)
    
    Returns:
        mst_edges: List of edges that form the MST
        total_weight: The sum of weights in the MST
        steps: A list of states for visualization purposes
    """
    # 1. Sort all edges in non-decreasing order of their weight
    # Complexity: O(E log E)
    sorted_edges = sorted(edges, key=lambda item: item[2])
    
    dsu = DisjointSetUnion(nodes)
    mst_edges = []
    total_weight = 0
    steps = [] # To record the process for visualization

    for u, v, weight in sorted_edges:
        # 2. Pick the smallest edge and check if it forms a cycle with the MST so far
        # We do this by checking if u and v have the same root in DSU
        if dsu.find(u) != dsu.find(v):
            # 3. If no cycle is formed, include this edge in MST
            dsu.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight
            # Record success
            steps.append({'edge': (u, v), 'weight': weight, 'status': 'accepted', 'current_mst': list(mst_edges)})
        else:
            # Record rejection (cycle detected)
            steps.append({'edge': (u, v), 'weight': weight, 'status': 'rejected', 'current_mst': list(mst_edges)})

    return mst_edges, total_weight, steps

def visualize_kruskal(nodes, edges, steps):
    """Visualizes the Kruskal's algorithm step by step."""
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42) # Consistent layout
    
    # Plotting loop
    for i, step in enumerate(steps):
        plt.figure(figsize=(10, 7))
        u, v = step['edge']
        status = step['status']
        mst_edges = [(e[0], e[1]) for e in step['current_mst']]
        
        plt.title(f"Step {i+1}: Testing Edge ({u}, {v}) with weight {step['weight']}\n"
                  f"Status: {status.upper()}", fontsize=14, color='green' if status == 'accepted' else 'red')

        # Draw all nodes
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
        nx.draw_networkx_labels(G, pos)

        # Draw all original edges (faintly)
        nx.draw_networkx_edges(G, pos, edgelist=[(e[0], e[1]) for e in edges], 
                               width=1, alpha=0.3, edge_color='gray')

        # Highlight current MST edges in blue
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=4, edge_color='blue')

        # Highlight the edge being considered
        color = 'green' if status == 'accepted' else 'red'
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=6, edge_color=color)

        # Draw weights
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.axis('off')
        plt.show()

# --- EXAMPLE 1: Standard Graph ---
# Illustration of nodes and weighted connections
# Nodes: A, B, C, D, E, F
example_nodes = ['A', 'B', 'C', 'D', 'E', 'F']
example_edges = [
    ('A', 'B', 4), ('A', 'C', 4), ('B', 'C', 2),
    ('C', 'D', 3), ('C', 'E', 2), ('C', 'F', 4),
    ('D', 'F', 3), ('E', 'F', 3)
]

print("Starting Kruskal's Algorithm on Example Graph...")
mst, total, process_steps = kruskal_algorithm(example_nodes, example_edges)

print("\nMST Edges Found:")
for u, v, w in mst:
    print(f" {u} -- {v} (weight: {w})")
print(f"Total MST Weight: {total}")

# Uncomment the line below to run the visualization in a local environment with matplotlib
# visualize_kruskal(example_nodes, example_edges, process_steps)

# --- EXAMPLE 2: Disconnected Components (Forest) ---
# Kruskal's will naturally find the MST for each component (a Spanning Forest)
nodes_2 = ['X', 'Y', 'Z', 'W', 'Q']
edges_2 = [
    ('X', 'Y', 10), ('Y', 'Z', 5), # Component 1
    ('W', 'Q', 2)                  # Component 2
]
mst_2, total_2, _ = kruskal_algorithm(nodes_2, edges_2)
print(f"\nMST for Disconnected Graph: {mst_2}, Total: {total_2}")