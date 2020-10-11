# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                       #
#   Finds all of the neighbors for a set of a nodes on a graph          #
#   represented as a 2-dimensional array. Useful for finding            #
#   connected nodes when solving path-finding problems.                 #
#                                                                       #
#   Example:    maze = [                                                #
#                           ['S', 'O', 'X', 'O'],                       #
#                           ['X', 'O', 'X', 'X'],                       #
#                           ['O', 'O', 'X', 'X'],                       #
#                           ['O', 'F', 'X', 'X']                        #
#                       ]                                               #
#                               	                                #
#                       # Instantiate the graph.                        #
#                       graph = Graph(maze)                             #
#                                                                       #
#                       # Print the graph.                              #
#                       for row in graph.graph:                         #
#                           print(row)                                  #
#                                                                       #
#                       # Print the neighbors of each node.             #
#                       for key, value in graph.neighbors.items():      #
#                       	print(f"{key}: {value}")                #
#                                                                       #
#                                                                       #                                                                    #
#   Author: Tyler Hooks                                                 #
#                                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.dimensions = (len(graph), len(graph[0]))
        self.coordinates = []
        for row in range(len(graph)):
            for column in range(len(graph[row])):
                self.coordinates.append((row, column))
        self.neighbors = self.get_neighbors()
        
    def get_neighbors(self) -> dict:
        coordinates = self.coordinates
        neighbors = {}
        dimensions = self.dimensions
        for point in coordinates:
            neighbors[point] = []
            if point[0] >= 0 and point[0] < dimensions[0] - 1:
                neighbors[point].append((point[0] + 1, point[1]))
            if point[0] > 0 and point[0] <= dimensions[0] - 1:
                neighbors[point].append((point[0] - 1, point[1]))
            if point[1] >= 0 and point[1] < dimensions[1] - 1:
                neighbors[point].append((point[0], point[1] + 1))
            if point[1] > 0 and point[1] <= dimensions[1] - 1:
                neighbors[point].append((point[0], point[1] - 1))
            if point[0] > 0 and point[0] < dimensions[0] - 1 and point[1] > 0 and point[1] < dimensions[1] - 1:
                neighbors[point].append((point[0], point[1] + 1))
                neighbors[point].append((point[0], point[1] - 1))
                neighbors[point].append((point[0] + 1, point[1]))
                neighbors[point].append((point[0] - 1, point[1]))

            # Remove duplicate tuples.
            for key, value in neighbors.items():
                neighbors[key] = list(set(value))

        return neighbors
