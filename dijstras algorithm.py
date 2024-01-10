# finding shortest path of every node from source node in a graph using dijstras algorithm
# this algorithm use dist array and visited array traverse from source and and updates its neighbour values
#and from that finite values in dist we get small one and again add it to visited and update its neighbours
#dist and visited are helpfull to update distances and not repeat the already proccessed nodes
# repeat this in n times n = no. of nodes

from collections import defaultdict


class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def add(self,node,tup):
        self.graph[node].append(tup)
    
    def display(self,dist):
        for i,cost in enumerate(dist):
            print("{0} cost is {1}".format(i,cost))

    def minimum_node(self,dist,visited):

        mini = float('inf')
        index = 0
        for i in range(len(dist)):
            if dist[i] == float('inf') or visited[i] == True:
                continue
            else:
                val = dist[i]
                if val < mini :
                    mini = val
                    index = i
        return index
                


    def dijstras(self,src):

        dist = [float('inf')]*self.v

        visited = [False]*self.v

        dist[src] = 0
        for i in range(self.v):

            current_node = self.minimum_node(dist,visited)

            visited[current_node] = True

            for v ,cost in self.graph[current_node]:
                if visited[v] == False:  # handles and neglect th updatation for loop vertices
                    if dist[v] > cost + dist[current_node] :
                        dist[v] = cost + dist[current_node]
        self.display(dist)



g = Graph(5)
g.add(0,(1,2))
g.add(0,(2,1))
g.add(0,(3,1))
g.add(1,(2,3))
g.add(2,(3,2))
g.add(2,(4,3))
g.add(3,(4,1))
g.add(4,(3,2))
g.add(0,(4,0.5))

g.dijstras(0)

                

        




