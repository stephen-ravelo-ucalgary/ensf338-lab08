import graphviz

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def addNode(self, data):
        if data not in self.adjacency_list.keys():
            self.adjacency_list[data] = {}
        return data
    
    def removeNode(self, node):
        for key, neighbors in self.adjacency_list.items():
            if (node in neighbors):
                neighbors.pop(node)
        self.adjacency_list.pop(node)
    
    def addEdge(self, n1, n2, weight):
        self.adjacency_list[n1][n2] = weight
        self.adjacency_list[n2][n1] = weight
    
    def removeEdge(self, n1, n2):
        self.adjacency_list[n1].pop(n2)
        self.adjacency_list[n2].pop(n1)
    
    def importFromFile(self, file):
        graph = graphviz.Source.from_file(file)
        
        for line in graph:
            line = line.split()
            try:
                n1 = self.addNode(int(line[0]))
                n2 = self.addNode(int(line[2]))
                if len(line) > 3:
                    self.addEdge(n1, n2, int(''.join(char for char in line[3] if char.isdigit())))
                else:
                    self.addEdge(n1, n2, 1)
            except:
                continue
    
if __name__ == "__main__":
    graph = Graph()
    
    #graph.addNode(1)
    #graph.addNode(2)
    #graph.addNode(3)
    #print(graph.adjacency_list)
    #graph.addEdge(1, 2, 5)
    #print(graph.adjacency_list)
    #graph.removeEdge(1, 2)
    #print(graph.adjacency_list)
    
    graph.importFromFile("random.dot")
    
    print(graph.adjacency_list)