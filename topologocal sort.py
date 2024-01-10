# topologocal sort
from collections import defaultdict


class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
        
    def add(self,u,v):
        self.graph[u].append(v)

    def topo_sortUtil(self,node,visited,stack) :

        visited[node] = True

        for i in self.graph[node] :
            if visited[i] == False:
                self.topo_sortUtil(i,visited,stack)

        # it takes the edge(last) nodes of graph and all nodes are appended from last to first as dfs traverse above        
        stack.append(node)



    def topo_sort(self):
        stack = []
        visited = [False]*self.v
        for i in range(self.v):
            if visited[i] == False :
                self.topo_sortUtil(i,visited,stack)
        return stack[::-1]
        







v = 5 
g = Graph(v)
g.add(4,1)
g.add(4,0)
g.add(1,2)
g.add(2,3)


stack = g.topo_sort()
print("the topological order for {} nodes is :".format(v))

print(stack)