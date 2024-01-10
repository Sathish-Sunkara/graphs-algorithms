# all pair shortest path algorithm
#floyd warshalls algorithm

class Graph :
    def __init__(self,vertices,graph):
        self.v = vertices
        self.graph = graph

    def display(self,dist):
        print(dist)

    def warshall(self):

        #create dist matrix for the graph
        dist = [[0]*self.v for i in range(self.v)]
        for i in range(self.v):
            for j in range(self.v):
                dist[i][j] = self.graph[i][j]


        for k in range(self.v):

            for i in range(self.v):

                for j in range(self.v):

                    if ((dist[i][j] > (dist[i][k] + dist[k][j])) and (dist[i][k] != float('inf')) and (dist[j][k] != float('inf'))) :
                        dist[i][j] = dist[i][k] + dist[k][j]

        self.display(dist)

inf = float('inf')
graph = [[0,1,2,3,inf] , 
         [2,0,3,inf,7] ,
         [5,7 ,0,3,6] ,
         [inf,inf,5,0 ,9],
         [7,5,345,4,inf]]
g = Graph(5,graph)
g.warshall()
