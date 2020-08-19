"""
# Adjacency List
# this adjacency list doesn’t use any lists. The vertices collection is a dictionary which lets us access each collection of edges in O(1) constant time. 
# Because the edges are contained in a set we can check for the existence of edges in O(1) constant time.
"""
class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B"},
                            "B": {"C", "D"},
                            "C": {"E"},
                            "D": {"F", "G"},
                            "E": {"C"},
                            "F": {"C"},
                            "G": {"A", "F"}
                        }

"""
# adjacency matrix:
# this matrix as a two-dimensional array–a list of lists
# With this implementation, we get the benefit of built-in edge weights. 0 denotes no relationship, 
# but any other value that is present represents an edge label or edge weight. 
# The drawback is that we do not have a built-in association between the vertex values and their index.
"""
class Graph1:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]

"""
Takeaway: The worst case storage of an adjacency lists occurs when the graph is dense. 
In this case, the matrix and list representation have the same complexity (O(V^2)). 
However, for the general case, the list representation is usually more desirable. 
Also, since finding a vertex’s neighbors is a common task, and adjacency lists make this operation easier, 
adjacency lists are most often used to represent graphs.

Takeaway: Adding vertices is very inefficient for adjacency matrices but very efficient for adjacency lists. Complexity: O(V) time in Matrix and Complexity: O(1) time in List

Takeaway: Removing vertices is inefficient in both adjacency matrices and lists but more efficient in lists. Complexity: O(V^2) Matrix and Complexity: O(V) - List

Takeaway: Adding edges to both adjacency matrices and lists is very efficient. Complexity: O(1) for both

Takeaway: Removing edges from both adjacency matrices and lists is very efficient. Complexity: O(1) for both

Takeaway: Finding edges in both adjacency matrices and lists is very efficient. Complexity: O(1) for both

Takeaway: Fetching all edges is less efficient in an adjacency matrix than an adjacency list. Complexity: O(V) in Matrix and Complexity: O(1) in List

Summary

Let’s summarize all this complexity information in a table:
  	    Space 	Add Vert 	Remove Vert 	Add Edge 	Remove Edge 	Find Edge 	Get All Edges
Matrix 	O(V^2) 	 O(V) 	    O(V^2) 	         O(1) 	     O(1) 	         O(1) 	     O(V)
List 	O(V+E) 	 O(1) 	    O(V) 	         O(1) 	     O(1) 	         O(1) 	     O(1)

"""