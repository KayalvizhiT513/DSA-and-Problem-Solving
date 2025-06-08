class GraphNode:
    def __init__(self, nodename):
        self.nodename = nodename
        self.neighbours = []

class Graph:
    def __init__(self):
        self.node_list = []

    def get_node(self, nodename):
        for node in self.node_list:
            if node.nodename == nodename:
                return node
        return None

    def add_edge(self, nodename1, nodename2):
        node1 = self.get_node(nodename1)
        node2 = self.get_node(nodename2)

        if not node1:
            node1 = GraphNode(nodename1)
            self.node_list.append(node1)
        if not node2:
            node2 = GraphNode(nodename2)
            self.node_list.append(node2)

        if node2 not in node1.neighbours:
            node1.neighbours.append(node2)
        if node1 not in node2.neighbours:
            node2.neighbours.append(node1)

    def dfs(self, startname):
        start_node = self.get_node(startname)
        if not start_node:
            print("Start node is not found in the graph")
            return

        visited = set()

        def dfs_recursive(node):
            visited.add(node)
            print(node.nodename, end=' ')
            for neighbour in node.neighbours:
                if neighbour not in visited:
                    dfs_recursive(neighbour)

        dfs_recursive(start_node)

    def bfs(self, startname):
        start_node = self.get_node(startname)
        if not start_node:
            print("Start node is not found in the graph")
            return

        visited = set()
        queue = [start_node]
        visited.add(start_node)

        while queue:
            node = queue.pop(0)
            print(node.nodename, end=' ')
            for neighbour in node.neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def print_graph(self):
        for node in self.node_list:
            neighbour_names = [neighbour.nodename for neighbour in node.neighbours]
            print(f"{node.nodename} -> {', '.join(neighbour_names)}")

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'D')
graph.add_edge('D', 'E')
graph.add_edge('C', 'A')

print("All nodes in the Graph:")
graph.print_graph()

print("\nDepth First Search:")
graph.dfs('A')

print("\nBreadth First Search:")
graph.bfs('A')
            
