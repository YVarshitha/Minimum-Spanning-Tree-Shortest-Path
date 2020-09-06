from collections import defaultdict
import time
#Class to represent a graph
class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = []


    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])


    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])


    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)


        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot


        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):

        result =[]

        i = 0
        e = 0

        self.graph =  sorted(self.graph,key=lambda item: item[2])

        parent = [] ; rank = []


        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V -1 :


            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)


            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)

        print("Path and Edges cost")
        for u,v,weight  in result:

            print ("%d -- %d == %d" % (u,v,weight))


start = time.time()
g = Graph(7)
f = open ( 'sp.txt' , 'r')
l = []
l = [ line.split() for line in f]
print (l)
for i in range(len(l)):
    g.addEdge(int(l[i][0]),int(l[i][1]),int(l[i][2]))
g.KruskalMST()



g1 = Graph(7)
f = open ('samp2.txt' , 'r')
k = []
k = [ line.split() for line in f]
print (k)
j=0;
for j in range(len(k)):
    g1.addEdge(int(k[j][0]),int(k[j][1]),int(k[j][2]))
g1.KruskalMST()




g2 = Graph(7)
f = open ('samp3.txt' , 'r')
m = []
m = [ line.split() for line in f]
print (m)
a=0;
for a in range(len(m)):
    g2.addEdge(int(m[a][0]),int(m[a][1]),int(m[a][2]))
g2.KruskalMST()



g3 = Graph(7)
f = open ('krus4.txt' , 'r')
n = []
n = [ line.split() for line in f]
print (n)
b=0;
for b in range(len(n)):
    g3.addEdge(int(n[b][0]),int(n[b][1]),int(n[b][2]))
g3.KruskalMST()


end = time.time()
elapse = end - start
print("\n")
print("Running time of the algorithm")
print(elapse)
