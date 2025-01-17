from collections import defaultdict
import time
# Graph is represented using adjacency list. Every
# node of adjacency list contains vertex number of
# the vertex to which edge connects. It also contains
# weight of the edge
class Graph:
    def __init__(self,vertices):

        self.V = vertices # No. of vertices

        # dictionary containing adjacency List
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))


    # A recursive function used by shortestPath
    def topologicalSortUtil(self,v,visited,stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        if v in self.graph.keys():
            for node,weight in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node,visited,stack)

        # Push current vertex to stack which stores topological sort
        stack.append(v)


    ''' The function to find shortest paths from given vertex.
        It uses recursive topologicalSortUtil() to get topological
        sorting of given graph.'''
    def shortestPath(self, s):

        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]

        # Call the recursive helper function to store Topological
        # Sort starting from source vertice
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s,visited,stack)

        # Initialize distances to all vertices as infinite and
        # distance to source as 0
        dist = [float("Inf")] * (self.V)
        dist[s] = 0

        # Process vertices in topological order
        while stack:

            # Get the next vertex from topological order
            i = stack.pop()

            # Update distances of all adjacent vertices
            for node,weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        # Print the calculated shortest distances
        for i in range(self.V):
            print ("%d" %dist[i]) if dist[i] != float("Inf") else  "Inf" ,


start = time.time()
g = Graph(6)


f = open ('samp1.txt' , 'r')
l = []
l = [ line.split() for line in f]
print (l)
i=0;
for i in range(len(l)):
    g.addEdge(int(l[i][0]),int(l[i][1]),int(l[i][2]))

s = 0
print ("Following are shortest distances from source %d " % s)
g.shortestPath(s)


g1 = Graph(7)


f = open ('samp2.txt' , 'r')
k = []
k = [ line.split() for line in f]
print (k)
j=0;
for j in range(len(k)):
    g1.addEdge(int(k[j][0]),int(k[j][1]),int(k[j][2]))

s1 = 1
print ("Following are shortest distances from source %d " % s1)
g1.shortestPath(s1)



g2 = Graph(7)


f = open ('ss.txt' , 'r')
m = []
m = [ line.split() for line in f]
print (m)
a=0;
for a in range(len(m)):
    g2.addEdge(int(m[a][0]),int(m[a][1]),int(m[a][2]))

s2 = 4
print ("Following are shortest distances from source %d " % s2)
g2.shortestPath(s2)


g3 = Graph(7)


f = open ('samp4.txt' , 'r')
n = []
n = [ line.split() for line in f]
print (n)
b=0;
for b in range(len(n)):
    g3.addEdge(int(n[b][0]),int(n[b][1]),int(n[b][2]))

s3 = 1
print ("Following are shortest distances from source %d " % s3)
g3.shortestPath(s3)

end = time.time()
elapse = end - start
print("\n")
print("Running time of the algorithm")
print(elapse*100)
