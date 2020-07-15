## BFS

Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2 of this post). The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array. For simplicity, it is assumed that all vertices are reachable from the starting vertex.


##DFS

Handling Disconnected Graph

Solution: This will happen by handling a corner case.

The above code traverses only the vertices reachable from a given source vertex. All the vertices may not be reachable from a given vertex as in the case of a Disconnected graph. To do complete DFS traversal of such graphs, run DFS from all unvisited nodes after a DFS.
The recursive function remains the same.

Algorithm:
- Create a recursive function that takes the index of node and a visited array.
- Mark the current node as visited and print the node.
- Traverse all the adjacent and unmarked nodes and call the recursive function with index of adjacent node.
- Run a loop from 0 to number of vertices and check if the node is unvisited in previous DFS then call the recursive function with current node.