from collections import defaultdict 

class BfsTraverser: 
  # Constructor 
  def __init__(self): 
    self.visited = []
    self.end_search = False
  def BFS(self,graph, start_node, goal_node,heuristics):
    heuristics={}
    heuristics["SportsComplex"]=730
    heuristics["Siwaka"]=405
    heuristics["Ph.1A"]=380
    heuristics["Ph.1B"]=280
    heuristics["STC"]=213
    heuristics["Phase2"]=210
    heuristics["Phase3"]=160
    heuristics["J1"]=500
    heuristics["Mada"]=630
    heuristics["parkingLot"]=0

    queue = []
    queue.append(start_node)
    #print(queue)
    #set of visited nodes
    self.visited.append(start_node)
    while queue and not self.end_search: 
      # Dequeue a vertex from 
      s = queue.pop(0)          

      # Get all adjacent vertices of the 
      # dequeued vertex s. If an adjacent 
      # has not been visited, then mark it 
      # visited and enqueue it 
      explored = {}
      
      for i in list(graph[s]):                   
          explored[i] = heuristics[i]
          i = min(explored, key = explored.get)

      if i not in self.visited:
          #print ("Command; Drive from ",s," to " ,i, " Estate/Junction", end = "\n") 
          #print("Current Node is",i, " but the goal Node is ",goal_node)
          print ("Command; Drive to " ,i, " Estate/Junction", end = "\n")
          if i is goal_node:
            print("We have reached ",i," the final destination")
            self.visited.append(i)
            self.end_search = True
            break
          else:
            #print("Here",self.end_search)
            queue.append(i)
            #visited[i] = True
            self.visited.append(i)

