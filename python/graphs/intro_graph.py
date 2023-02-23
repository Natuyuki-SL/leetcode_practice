import os
os.system('clear')

class Graph:
    def __init__(self, edges):
        '''
        Edges are a list of possible routes as tuples
        '''
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                if end in self.graph_dict[start]:
                    pass
                else:
                    self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    
    def get_path(self, start, end, path = []):
        '''
        Acts as a recursive function to keep generating new valid paths
        '''
        # Auto add the current starting node to the current path
        path = path + [start]
        
        # Base case, return the path as a list for appending (when we can reached the end after recursive calls)
        if start == end:
            return [path]
        
        # If there are no possible paths
        if start not in self.graph_dict:
            return []

        # For the recursive functions to collect all the paths
        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path) # Recursion occurs here
            for n in new_paths:
                paths.append(n)
        
        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        '''
        Similar to get_path function, but we only return the shortest path from the final list
        '''
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path) 
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path = sp
        return shortest_path
            
routes = [
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto')
]

g1 = Graph(routes)
print(f'Graph dictionary - {g1.graph_dict}')
print()
start = input('Enter start: ')
end = input('Enter end: ')
print()
print(f'Paths between {start} and {end} :{g1.get_path(start, end)}')
print()
print(f'Shortest path between {start} and {end} :{g1.get_shortest_path(start, end)}')


