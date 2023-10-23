def bfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    print(start_node)

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C']
    }

    start_node = 'A'
    dfs(graph, start_node)

