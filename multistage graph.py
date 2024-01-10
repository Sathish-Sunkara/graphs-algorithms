#shortest path from source to destination using multistage graph algorithm
#it takes destination node cost as 0 and update values of nodes which are at previous level (means nodes that connect finale node)
#like above it back chaining the updatation of costs using edge costs and node values finally we reach the source node with some value
#we maintain a dist array to update the values of nodes from back side 
class Graph:
    def __init__(self,v,graph):
        self.v = v
        self.graph = graph

    def shortest(self):
        dist = [float("inf")]*self.v  # tracking and upadte the cost from destination node
        dist[self.v-1] = 0            # destination node cost
        for i in range(self.v-2 , -1 , -1):    # updating cost infinity to some value her only nodes that connects the destination node will be updated other nodes are not
            node = i
            dist[i] = float('inf')
            for j in range(self.v):
                if graph[node][j] == float('inf') :    # no edge is there update no update needed
                    continue
                dist[i] = min(dist[i] , self.graph[node][j] + dist[j])   #main function that is upading values on nodes form child nodes
        return dist[0]   # it is type of DP problem 
    
v = 8
inf = float("inf")
graph = [
         [inf,1,1,3,inf,inf,inf,inf] ,
         [inf,inf,inf,inf,2,4,inf,inf] ,
         [inf,inf,inf,inf,6,1,6,inf] , 
         [inf,inf,inf,inf,inf,inf,2,inf] , 
         [inf,inf,inf,inf,inf,inf,inf,8],
         [inf,inf,inf,inf,inf,inf,inf,4],
         [inf,inf,inf,inf,inf,inf,inf,1]
         ]

g = Graph(v,graph)
print(g.shortest())



  
