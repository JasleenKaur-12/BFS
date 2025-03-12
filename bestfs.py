import heapq


class Node:
    def __init__(self, id, heuristic):
        self.id = id
        self.heuristic = heuristic
        self.visited = False
    
    def __lt__(self, other):
      
        return self.heuristic < other.heuristic


def best_first_search(graph, start_id, goal_id):
    
    open_list = []
    
  
    start_node = graph[start_id]
    start_node.visited = True
    heapq.heappush(open_list, start_node)
    
    while open_list:
    
        current_node = heapq.heappop(open_list)
        print(f"Visiting node {current_node.id} with heuristic value {current_node.heuristic}")
        
     
        if current_node.id == goal_id:
            print(f"Goal node {current_node.id} found!")
            return
        
    
        for neighbor in graph:
            if not neighbor.visited:
                neighbor.visited = True
                heapq.heappush(open_list, neighbor)
    
    print("Goal node not found.")

# Main function
def main():
   
    graph = [
        Node(0, 5),  
        Node(1, 2), 
        Node(2, 8), 
        Node(3, 3),  
        Node(4, 1),  
        Node(5, 0)   
    ]
    
    start_id = 0 
    goal_id = 3  

   
    best_first_search(graph, start_id, goal_id)

if __name__ == "__main__":
    main()
