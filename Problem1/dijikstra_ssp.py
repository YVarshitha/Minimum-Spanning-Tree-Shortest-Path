import sys
import time

from collections import defaultdict

class Graph:

	def minDistance(self, dist, queue):
		minimum = float("Inf")
		min_index = -1

		for i in range(len(dist)):
			if dist[i] < minimum and i in queue:
				minimum = dist[i]
				min_index = i
		return min_index


	def printPath(self, parent, j):

		if parent[j] == -1 :
			print (j),
			return
		self.printPath(parent, parent[j])
		print (j),


	def printSolution(self, src, dist, parent):
		print("Vertex \t\t\tDistance from Source \tPath")
		for i in range(0, len(dist)):
			print("\n%d --> %d \t\t%d \t\t\t\t\t\t\t\t" % (src, i, dist[i])),
			self.printPath(parent,i)


	def dijkstra(self, graph, src):

		row = len(graph)
		col = len(graph[0])

		dist = [float("Inf")] * row

		parent = [-1] * row

		dist[src] = 0

		queue = []
		for i in range(row):
			queue.append(i)

		while queue:
			u = self.minDistance(dist,queue)
			queue.remove(u)

			for i in range(col):
				if graph[u][i] and i in queue:
					if dist[u] + graph[u][i] < dist[i]:
						dist[i] = dist[u] + graph[u][i]
						parent[i] = u

		self.printSolution(src, dist,parent)
start = time.time()
file = open("Directed Graph1.txt", "r")
V, E, graph_type = file.readline().strip().split(' ')
matrix = [[0 for x in range(int(V))] for y in range(int(V))]

for i in range(int(E)):
    v1, v2, weight = file.readline().strip().split(' ')
    matrix[int(v1)][int(v2)] = int(weight)
    if graph_type == 'U':
      matrix[int(v2)][int(v1)] = int(weight)

source = file.readline().strip()
file.close()
g= Graph()

if source == '':
  g.dijkstra(matrix,0)
else:
  g.dijkstra(matrix, int(source))


file1 = open("Directed Graph2.txt", "r")
V, E, graph_type = file1.readline().strip().split(' ')
matrix1 = [[0 for x in range(int(V))] for y in range(int(V))]

for j in range(int(E)):
    v1, v2, weight = file1.readline().strip().split(' ')
    matrix1[int(v1)][int(v2)] = int(weight)
    if graph_type == 'U':
      matrix1[int(v2)][int(v1)] = int(weight)

source1 = file1.readline().strip()
file1.close()
g1= Graph()

if source1 == '':
  g1.dijkstra(matrix1,0)
else:
  g1.dijkstra(matrix1, int(source))


file2 = open("Undirected Graph1.txt", "r")
V, E, graph_type = file2.readline().strip().split(' ')
matrix2 = [[0 for x in range(int(V))] for y in range(int(V))]

for k in range(int(E)):
    v1, v2, weight = file2.readline().strip().split(' ')
    matrix2[int(v1)][int(v2)] = int(weight)
    if graph_type == 'U':
      matrix2[int(v2)][int(v1)] = int(weight)

source2 = file2.readline().strip()
file2.close()
g2= Graph()

if source2 == '':
  g2.dijkstra(matrix2,0)
else:
  g2.dijkstra(matrix2, int(source))


file3 = open("Undirected Graph2.txt", "r")
V, E, graph_type = file3.readline().strip().split(' ')
matrix3 = [[0 for x in range(int(V))] for y in range(int(V))]

for a in range(int(E)):
    v1, v2, weight = file3.readline().strip().split(' ')
    matrix3[int(v1)][int(v2)] = int(weight)
    if graph_type == 'U':
      matrix3[int(v2)][int(v1)] = int(weight)

source3 = file3.readline().strip()
file3.close()
g3= Graph()

if source3 == '':
  g3.dijkstra(matrix3,0)
else:
  g3.dijkstra(matrix3, int(source))


end = time.time()
elapse = end - start
print("\n")
print("Running time of the algorithm")
print(elapse)
