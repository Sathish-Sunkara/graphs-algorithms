#nodes which splits the graph into 2 or more parts

from collections import defaultdict


class Graph :
    def __init__(self,v):
        self.v = v 
        self.graph = defaultdict(list)
        self.time = 0

    def add(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def apUtil(self,u,visited,ap,parent,low,disc) :
        children = 0

        visited[u] = True

        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        #recur all nodes to adjecent to u
        for v in self.graph[u] :
            if visited[v] == False :
                parent[v] = u
                children += 1
                self.apUtil(v,visited,ap,parent,low,disc)

                low[u] = min(low[u],low[v])

                if parent[u] == -1 and children > 1 :
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u] :
                    ap[u] = True

            elif v != parent[u] :
                low[u] = min(low[u] , disc[v])
                





    def ap(self):
        visited = [False]*self.v
        disc = [float('inf')]*self.v
        low = [float('inf')] * self.v
        parent = [-1] * self.v
        ap = [False] * self.v

        for i in range(self.v):
            if visited[i] == False :
                self.apUtil(i,visited,ap,parent,low,disc)

        for index , value in enumerate(ap):
            if value == True :
                print(index , end = "  ")



g = Graph(5)
g.add(1,0)
g.add(0,2)
g.add(2,1)
g.add(0,3)
g.add(3,4)
g.ap()

