#this code detects cycles in undirected graph 
from collections import defaultdict


class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)



    def iscyclicutil(self,node,visited,parent):
        visited[node] = True
        for i in self.graph[node] :
            if visited[i] == False:
                if self.iscyclicutil(i,visited,node) :
                    return True
            elif i != parent :
                return True
        return False
    def iscyclic(self):
        visited = [False] * self.v
        for i in range(self.v) :
            if visited[i] == False:
                if self.iscyclicutil(i,visited,-1) :
                    return True
        return False
    

g = Graph(5)

g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,3)
g.addedge(3,4)
g.addedge(4,0)




if g.iscyclic() == True :
    print("the graph has cycles")
else:
    print("graph has no cycles")






        