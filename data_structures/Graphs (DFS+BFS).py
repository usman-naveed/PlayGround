from collections import deque as dq


class Graph:
    def __init__(self, adj_list=None):
        if adj_list:
            self.adj_list = adj_list
        else:
            self.adj_list = dict()

    def print_all_edges(self):
        edges = []
        if self.adj_list:
            for i in self.adj_list.keys():
                for j in self.adj_list[i]:
                    edges.append({i, j})
        return edges

    def get_nodes(self):
        return list(self.adj_list.keys())

    def add_node(self):
        pass

    def add_edge(self):
        pass

    def bfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        queue = dq(start_node)
        while queue:
            node = queue.popleft()
            print(node)
            for i in self.adj_list[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return

    def dfs(self, start_point, visited=None):
        if visited is None:
            visited = set()
        for node in self.adj_list[start_point]:
            if start_point not in visited:
                print(start_point)
                visited.add(start_point)
            if node not in visited:
                print(node)
                visited.add(node)
                self.dfs(node, visited)
        return


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E", "O", "I", "G"],
    "G": ["F", "H"],
    "H": ["G"],
    "I": ["F", "J"],
    "O": ["F"],
    "J": ["K", "L", "I"],
    "K": ["J"],
    "L": ["J"]
}
g = Graph(graph)
#g.dfs('A')
g.bfs('A')
# print(g.print_all_edges())
# print(g.get_nodes())
