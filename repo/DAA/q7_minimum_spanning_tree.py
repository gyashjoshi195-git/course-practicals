"""Q7: Minimum Spanning Tree using Kruskal's and Prim's algorithms.

Example graph (vertices 0..4):
  0-1 (2), 0-3 (6), 1-2 (3), 1-3 (8), 1-4 (5), 2-4 (7), 3-4 (9)
"""
import heapq

edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
V = 5


# ---------- Kruskal (sort edges + Union-Find) ----------
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def kruskal(V, edges):
    parent = list(range(V))
    mst, cost = [], 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        ru, rv = find(parent, u), find(parent, v)
        if ru != rv:               # adding edge does not form a cycle
            parent[ru] = rv
            mst.append((u, v, w))
            cost += w
    return mst, cost


# ---------- Prim (grow tree using min-heap) ----------
def prim(V, edges, start=0):
    adj = {i: [] for i in range(V)}
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))
    visited, mst, cost = {start}, [], 0
    heap = [(w, start, v) for w, v in adj[start]]
    heapq.heapify(heap)
    while heap and len(visited) < V:
        w, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, w))
        cost += w
        for w2, nxt in adj[v]:
            if nxt not in visited:
                heapq.heappush(heap, (w2, v, nxt))
    return mst, cost


if __name__ == "__main__":
    m, c = kruskal(V, edges)
    print("Kruskal MST edges:", m, "| total cost =", c)
    m, c = prim(V, edges)
    print("Prim    MST edges:", m, "| total cost =", c)
