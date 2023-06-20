from Queue import Queue

class GraphSearch:
    def __init__(self, graph):
        self.graph = graph
        self.output = []

    def dfsIterative(self, start_node):
        # Initialize a visited set
        visited = set()

        # Initialize the stack
        stack = [start_node]

        # While the stack is not empty
        while stack:
            # Pop the top node
            node = stack.pop()

            # If the node has not been visited
            if node not in visited:
                # Process node
                print("Visiting:", node)
                self.output.append(node)
                
                # Add node to visited
                visited.add(node)

                # Add neighbors to the stack
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        
    def dfsRecursive(self, start_node, visited=None):
        if visited is None:
            visited = set()

        # Process node
        print(start_node)
        self.output.append(start_node)

        # Add node to visited
        visited.add(start_node)

        # Recurse on neighbors
        for neighbor in self.graph[start_node]:
            if neighbor not in visited:
                self.dfsRecursive(neighbor, visited)

    def bfsIterative(self, start_node): 
        # Initialize a visited set
        visited = set()

        # Initialize the queue
        queue = Queue()
        queue.enqueue(start_node)

        # While the queue is not empty
        while not queue.is_empty():
            # Dequeue the front node
            node = queue.dequeue()

            # If the node has not been visited
            if node not in visited:
                # Process node
                print("Visiting:", node)
                self.output.append(node)

                # Add node to visited
                visited.add(node)

                # Add neighbors to the queue
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)


    def bfs(self, queue, visited):
        # Base case: if the queue is empty, return
        if queue.is_empty():
            return

        # Process the front node
        node = queue.dequeue()
        print("Visiting:", node)
        self.output.append(node)

        # Add neighbors to the queue
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

        # Recurse with the updated queue and visited set
        self.bfs(queue, visited)


    def bfsRecursive(self, start_node):
        # Function to call bfs
        visited = set([start_node])
        queue = Queue()
        queue.enqueue(start_node)
        self.bfs(queue, visited)
