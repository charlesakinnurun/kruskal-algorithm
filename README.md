<h1 align="center">Kruskal’s Algorithm</h1>

## Overview

**Kruskal’s Algorithm** is a **greedy algorithm** used to find the **Minimum Spanning Tree (MST)** of a **weighted, undirected graph**.

A **Minimum Spanning Tree** is a subset of edges that:

* Connects **all vertices**
* Contains **no cycles**
* Has the **minimum total edge weight**

Unlike Prim’s Algorithm, **Kruskal’s Algorithm works by selecting the smallest edges first**, ensuring that no cycle is formed.

<a href="/src/main.py">Check out for source code.</a>

---

## 📌 Key Concepts

### Graph

A structure made of **vertices (nodes)** connected by **edges**.

### Weighted Graph

A graph where each edge has a **weight or cost**.

### Minimum Spanning Tree (MST)

A tree that connects all vertices with **minimum total edge weight**.

For a graph with **V vertices**, the MST will contain:

```
V - 1 edges
```

---

## ⚙️ How Kruskal’s Algorithm Works

1. Sort all edges in **ascending order of weight**
2. Pick the **smallest edge**
3. Check if adding the edge creates a **cycle**
4. If **no cycle**, include it in the MST
5. If **cycle occurs**, discard the edge
6. Repeat until the MST contains **V − 1 edges**

To efficiently detect cycles, Kruskal's Algorithm uses a **Union-Find (Disjoint Set)** data structure.

---

## 🧩 Example Graph

```
       4
   A ------- B
   |         |
  3|         |5
   |         |
   C ------- D
        2
```

### Edge Weights

| Edge | Weight |
| ---- | ------ |
| A–B  | 4      |
| A–C  | 3      |
| B–D  | 5      |
| C–D  | 2      |

---

## 🧪 Step-by-Step Example

### Step 1 — Sort Edges by Weight

```
C–D (2)
A–C (3)
A–B (4)
B–D (5)
```

---

### Step 2 — Build the MST

#### Add C–D (2)

```
MST = {C–D}
```

No cycle.

---

#### Add A–C (3)

```
MST = {C–D, A–C}
```

No cycle.

---

#### Add A–B (4)

```
MST = {C–D, A–C, A–B}
```

Now all vertices are connected.

---

### Final Minimum Spanning Tree

Edges:

```
C – D (2)
A – C (3)
A – B (4)
```

### Total Weight

```
2 + 3 + 4 = 9
```

---

## ⏱️ Time & Space Complexity

| Operation             | Complexity |
| --------------------- | ---------- |
| Sorting edges         | O(E log E) |
| Union-Find operations | O(E α(V))  |

Overall Complexity:

```
O(E log E)
```

Where:

* **V** = number of vertices
* **E** = number of edges
* **α(V)** = inverse Ackermann function (very small)

**Space Complexity:** O(V)

---

## 🧠 Python Implementation

```python
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 != root2:
            self.parent[root2] = root1


def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)

    mst = []

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst


vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 4),
    ('A', 'C', 3),
    ('B', 'D', 5),
    ('C', 'D', 2)
]

print(kruskal(vertices, edges))
```

### Output

```
[('C', 'D', 2), ('A', 'C', 3), ('A', 'B', 4)]
```

---

## 👍 Advantages

* Simple and easy to understand
* Efficient for **sparse graphs**
* Guarantees the **minimum spanning tree**

---

## 👎 Disadvantages

* Sorting edges can be costly for **very large graphs**
* Requires **Union-Find data structure**
* Not ideal for **dense graphs**

---

## 📊 Kruskal’s vs Prim’s Algorithm

| Feature         | Kruskal’s Algorithm | Prim’s Algorithm    |
| --------------- | ------------------- | ------------------- |
| Strategy        | Edge-based          | Vertex-based        |
| Approach        | Sort edges globally | Expand tree locally |
| Best for        | Sparse graphs       | Dense graphs        |
| Data structures | Union-Find          | Priority Queue      |

---

## 📌 When to Use Kruskal’s Algorithm

Use Kruskal’s Algorithm when:

* The graph is **sparse**
* You need to construct a **Minimum Spanning Tree**
* You have a list of **edges rather than adjacency structure**

Common applications include:

* Network design
* Road construction planning
* Cluster analysis
* Telecommunications networks

---

## 🏁 Summary

Kruskal’s Algorithm is a powerful greedy algorithm used to find a **Minimum Spanning Tree**. By always selecting the smallest edge that does not create a cycle, it ensures the final tree connects all vertices with the **lowest possible cost**.
