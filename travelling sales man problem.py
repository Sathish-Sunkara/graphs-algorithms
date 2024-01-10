# first thing is undirected weighted graph
# it is complete graph that means there is edge between every pair of nodes (i.e: there exists hamiltonion cycles)

from itertools import permutations


class Graph:
    def __init__(self,v,graph):
        self.v = v
        self.graph = graph

    def TSP(self,src):
        vertex = []
        for i in range(self.v):
            if i !=  src :
                vertex.append(i)
        # all_paths stores the possible paths
        all_paths = permutations(vertex)
        # check for each path

        min_cost = float('inf')         # stores final min cost
        path_weight = 0                 # stores single path weight 

        for path in all_paths :
            path_weight = 0
            i = src
            for j in path :
                path_weight += self.graph[i][j]
                i = j
            path_weight += self.graph[i][src]

            min_cost = min(min_cost , path_weight)
        return min_cost

        


v = 4
# representing with matrix is good for complete graph (bcoz cost is retrives easily with [i][j] technic) 
graph = [
    [0,10,15,20] , 
    [10,0,35,25] , 
    [15,35,0,30] , 
    [20,25,30,0]
        ]
src = 1
g = Graph(v,graph)
print(g.TSP(0))