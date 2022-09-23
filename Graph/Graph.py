#Graph Data Structure
class Graph:
    #Graph Constructor
    def __init__(self):
        self.adj_list = {}
    
    #function to add a vertex 
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    #function to print adjacency list of the graph
    def print_graph(self):
        for vertex in self.adj_list.keys():
            print(vertex, " : ", self.adj_list[vertex])

    #function to add edge between two vertices
    def add_edge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    #function to remove edge between two vertices
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    #function to remove a vertex
    def remove_vertex(self,v):
        if v in self.adj_list.keys():
            for other_vertex in self.adj_list[v] :
                self.adj_list[other_vertex].remove(v)
            del self.adj_list[v]
            return True
        return False



#Demo Operations 
my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')
my_graph.add_edge('A','D')

my_graph.print_graph()

my_graph.remove_vertex('D')

my_graph.print_graph()
