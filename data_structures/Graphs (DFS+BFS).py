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
                    edges.append((i, j))
        return edges

    def get_nodes(self):
        return list(self.adj_list.keys())

    def add_node(self):
        pass

    def add_edge(self):
        pass

    def bfs(self):
        pass

    def dfs(self):
        pass

graph = {"a": ["b", "c"],
         "b": ["a", "d"],
         "c": ["a", "d"],
         "d": ["e"],
         "e": ["d"]
         }
g = Graph(graph)
print(g.print_all_edges())
print(g.get_nodes())
