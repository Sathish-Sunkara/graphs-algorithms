#khans algorithm for topologocal sort
#maintain a indegree list and take 0 degree elements and add them and also update its neighbours indegree every time 


from collections import defaultdict


class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
    
    def add(self,u,v):
        self.graph[u].append(v)

    def topo(self):

        indegree = [0]*self.v

        #making in degree
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j] += 1

        #take queue that have indegree 0 nodes
        que = []
        #fill queue with 0 indegree nodes
        for i in range(self.v):
            if indegree[i] == 0:
                que.append(i)

        result = []

        count =0
        while que:

            node = que.pop(0)

            result.append(node)

            for i in self.graph[node]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    que.append(i)
            count += 1

        if count != self.v :
            return "there is a cycle in the graph no ordering is possible"
        return result
    

g = Graph(6)
g.add(5,2)
g.add(5,0)
g.add(4,0)
g.add(4,1)
g.add(2,3)
g.add(3,1)
result = g.topo()
print('result is : ')
print(result)





        


