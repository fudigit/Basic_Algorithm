'''
build node_to_neigh and node_to_degree in one pass
# issues:
# 1. node all nodes in seqs are captures, [[1]] will be missed
# 2. use org to initialize the nodes and edges, it creates nodes that seqs don't have
# work around: create a set to capture all the actual nodes in seqs, compare with org
# better solution: create graph from seqs, not org
'''

from collections import deque

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):

        # get the graph (nodes and edges), count indegree
        # slow way, define 2 dict and 1 hashset
        node_to_indegree = {n: 0 for n in org}
        node_to_neigh = {n: [] for n in org}
        exist_edge = set()
        nodes_seq = set()
        for s in seqs:
            # get all unique nodes in seqs
            nodes_seq = nodes_seq | set(s)
            for i in range(len(s)-1):
                # since the nodes is initialized by org, check if seqs has invalid nodes
                if s[i] not in node_to_neigh or s[i+1] not in node_to_neigh:
                    return False
                elif (s[i],s[i+1]) not in exist_edge:
                    exist_edge.add((s[i],s[i+1]))
                    node_to_neigh[s[i]].append(s[i+1])
                    node_to_indegree[s[i+1]] += 1
        
        #print(node_to_indegree, node_to_neigh)
        
        # topological sorting
        start_node = [n for n in org if node_to_indegree[n] ==0]

        queue = deque(start_node)
        re_seq = []
        
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            re_seq.append(node)
            for neigh in node_to_neigh[node]:
                node_to_indegree[neigh] -= 1
                if node_to_indegree[neigh] == 0:
                    queue.append(neigh)
        #print(re_seq)
        
        # check if the result is org
        if org == re_seq and nodes_seq == set(org):
            return True
        return False
