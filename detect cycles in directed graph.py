from collections import defaultdict
# it detects the cycles in directed graph

class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def iscyclicutil(self,node,visited,recstack):
        visited[node] = True
        recstack[node] = True

        for i in self.graph[node] :
            if visited[i] == False:
                if self.iscyclicutil(i,visited,recstack) :
                    return True
            elif recstack[i] == True :
                return True
        recstack[node] = False
        return False
    def iscyclic(self):
        visited = [False] * (self.v + 1)
        recstack = [False] * (self.v + 1)
        for i in range(self.v) :
            if self.iscyclicutil(i,visited,recstack) :
                return True
        return False
    

g = Graph(7)

g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,3)
g.addedge(3,4)



if g.iscyclic() == True :
    print("the graph has cycles")
else:
    print("graph has no cycles")






        