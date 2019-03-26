"""
BFS
1. find all nodes: given the root nodes, using BFS. Use hashset to avoid repeated nodes
2. clone nodes with label only: create a mapping between old nodes -> cloned nodes
3. clone the neighbors for each clined node: neighbors are also cloned nodes



Note: 
1. change to the cloned object doesn't impacted the original object. A and clone A are stored
in different places
2. DFS may stack overflow, DFS uses recursion
stack memory = ?; heap memory = RAM
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from collections import deque

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node is None:
            return node
        
        
        # one node to find all nodes
        root = node
    
        # 1. use BFS to find all the nodes
        #   a. add root node to queue, also to the set (set is used to avoid duplicates)
        #   b. in each round, pop a node in the queue, and add its non-repeating neighbor nodes to the queue, as well as to the set. Until no nodes in the queue
        all_nodes = self.getNode(root)
    
        # 2. copy all the nodes, store the mapping from old -> new nodes in a hashmap
        #   a. put each node in nodes into dict, set it as the key, create a clone node as the value
        mapping = {}
        for node in all_nodes:
            mapping[node] = UndirectedGraphNode(node.label)
    
    
        # 3. copy the neighbor nodes for each cloned node
        #   a. for each oiginal node, it has a list of neighor nodes, add each of them to the cloned node's neighbors
        for node in all_nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[root]
    
    
    
    # step 1 function to get all nodes
    def getNode(self, node):
        queue = collections.deque([node])
        all_nodes = set([node])
        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor not in all_nodes:
                    all_nodes.add(neighbor) 
                    queue.append(neighbor)
        return all_nodes
        
        
        
        
        
        
        
        
        
        
        
