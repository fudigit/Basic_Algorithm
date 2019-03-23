'''
Topological sorting using BFS
1. count indegree for all nodes
2. put independent nodes into queue for bfs
3. (kill node and its eges) add each node in queue to topological list, visit its neighbors, reduce their indegree
4. add neighbor nodes with 0 indegree to queue 
'''

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # 1. count the indegree for all nodes
        node_to_indegree = self.get_indegree(graph)
        
        # 2. put independent nodes (indegree is 0) into the queue
        start_nodes = [node for node in graph if node_to_indegree[node] == 0]
        queue = deque(start_nodes)
        
        # 3. take out the nodes in the queue 1 by 1, and put them into the topological order
        #    visit the neighbors of the node being taken out, reduce their indegree by 1
        # 4. when a neighbor's indegree is 1, put it into the queue
        topo_order = []
        while queue:
            node_ind = queue.popleft()
            topo_order.append(node_ind)
            for neighbor in node_ind.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return topo_order
        
        
        
    def get_indegree(self, graph):
        # initialize a mapping from node to indegree
        node_to_indegree = {node: 0 for node in graph}
        # each neighbor of a node indicate 1 indegree for that neighbor!
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
                
        return node_to_indegree
        
