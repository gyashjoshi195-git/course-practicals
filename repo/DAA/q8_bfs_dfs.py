"""Q8: Graph traversal using BFS and DFS.

Example graph (adjacency list):
  A: B, C | B: D, E | C: F | D: - | E: F | F: -
BFS uses a queue (level by level), DFS uses a stack/recursion (deep first).
Time: O(V + E)
"""
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


def bfs(graph, start):
    visited, order = {start}, []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return order


def dfs(graph, node, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(node)
    order.append(node)
    for nb in graph[node]:
        if nb not in visited:
            dfs(graph, nb, visited, order)
    return order


if __name__ == "__main__":
    print("BFS from A:", " -> ".join(bfs(graph, "A")))  # A B C D E F
    print("DFS from A:", " -> ".join(dfs(graph, "A")))  # A B D E F C
