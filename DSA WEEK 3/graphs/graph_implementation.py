# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_vertex(self, data):
#         if data not in self.graph:
#             self.graph[data] = []

#     def insert(self, vertex, edge, is_bidirectional=True):
#         self.add_vertex(vertex)
#         self.add_vertex(edge)
#         self.graph[vertex].append(edge)
#         if is_bidirectional:
#             self.graph[edge].append(vertex)

#     def display(self):
#         for vertex in self.graph:
#             print(f'{vertex}: {self.graph[vertex]}')

#     def get_vertices(self):
#         return list(self.graph.keys())

#     def get_edges(self):
#         edges = []
#         for vertex in self.graph:
#             for edge in self.graph[vertex]:
#                 edges.append((vertex, edge))
#         return edges

# # Test the Graph class
# g = Graph()
# g.add_vertex('A')
# g.insert(vertex='A', edge='B', is_bidirectional=True)
# g.insert(vertex='A', edge='C', is_bidirectional=True)
# g.insert(vertex='B', edge='B', is_bidirectional=False)
# g.display()

# print("Vertices:", g.get_vertices())
# print("Edges:", g.get_edges())

#...............................................amulyas .....................................................

# def add_node(v):
#     global node_count
#     if v in nodes:
#         print(v,"is already present in the graph")
#     else:
#         node_count=node_count+1
#         nodes.append(v)
#         for n in graph:
#           n.append(0)
#         temp=[]
#         for i  in range(node_count):
#             temp.append(0)
#         graph.append(temp)
# def add_edge(v1,v2):
#     if v1 not in nodes:
#         print(v1,"is not present in the graph")
#     elif v2 not in nodes:
#         print(v2,"is not present in the graph")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = 1
#         graph[index2][index1] = 1
#..............................................too give weight to the graph.........................................
# def add_edge(v1,v2,cost):
#     if v1 not in nodes:
#         print(v1,"is not present in the graph")
#     elif v2 not in nodes:
#         print(v2,"is not present in the graph")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = cost
#         graph[index2][index1] = cost


# def add_node(v):
#     if v in graph:
#         print(v,"is already present in the graph")
#     else:
#         graph[v] = []

# graph={}

# print(graph)

# def add_edge(v1,v2):
#     if v1  not in graph:
#         print(v1,"is  not present in the graph")
#     elif v2 not in graph:
#         print(v2,"is not present in the graph")
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)

# def delete_node(v):
#     global node_count
#     if v not in nodes:
#         print(v,"is not present in the graph")
#     else:
#         index1=nodes.index(v)
#         node_count=node_count-1
#         nodes.remove(v)
#         graph.pop(index1)
#         for i in graph:
#             i.pop(index1)
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(format (graph[i][j]),end=" ")
        # print()
# def delete_edge(v1,v2):
#     if v1 not in graph:
#         print(v1,"is not in the graph")
#     elif v2 not in nodes:
#         print(v2,"is not present in graph")
#     else:
#         index1 = nodes.index(v1)
#         index2 =nodes.index(v2)
#         graph[index1][index2]=0
#         graph[index2][index1]=0
 
        


#...............................undirected ,weighted graph........................
# def add_edge(v1,v2,cost):
#     if v1  not in graph:
#         print(v1,"is  not present in the graph")
#     elif v2 not in graph:
#         print(v2,"is not present in the graph")
#     else:
#         list1=[v2,cost]
#         list2=[v1,cost]
#         graph[v1].append(list1)
#         graph[v2].append(list2)
#....................................directed graph.................................
# def add_edge(v1,v2):
#     if v1  not in graph:
#         print(v1,"is  not present in the graph")
#     elif v2 not in graph:
#         print(v2,"is not present in the graph")
#     else:
#         graph[v1].append(v2)
# def delete_node(v):
#     if v not in graph:
#         print(v,"is not present in thw graph")
#     else:
#         graph.pop(v)
#         for i in graph:
#             list1 = graph[i]
#             if v in list1:
#                 list1.remove(v)
# graph = {}
# add_node("A")
# add_node("B")

# add_node("C")
# add_edge("A","B",10)
# delete_node("A")
# add_edge("A","C")
# print(graph)

# nodes=[]
# graph=[]
# node_count=0
# print("before")
# print(nodes)
# print(graph)
# add_node("A")
# add_node("B")
# add_node("C")
# add_edge("A","B",10)
# add_edge("A","C",5)
# print("after")
# print("nodes:",nodes)
# print(graph)
# print_graph()


