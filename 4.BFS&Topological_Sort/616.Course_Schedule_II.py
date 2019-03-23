from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        
        
        # 1. count indegree
        # 2. put independent nodes into queue
        # 3. bfs the nodes, add to order, reduce its neighbor indegree
        # 4. put neighbor to queue if indegree is 0
        
        # here need both indegree and the neighbor for each course
        
        # get mapping of course to indegree, get course neighbors
        course_to_indegree = {c: 0 for c in range(numCourses)}
        course_neigh = [[] for _ in range(numCourses)]
        for to_c, pre_c in prerequisites:
            course_to_indegree[to_c] += 1
            course_neigh[pre_c].append(to_c)
        
        # put ind courses into queue
        queue = deque()
        for c in range(numCourses):
            if course_to_indegree[c] == 0:
                queue.append(c)
        
        # topological sorting using bfs
        order = []
        while queue:
            c_ind = queue.popleft()
            order.append(c_ind)
            for neighbor in course_neigh[c_ind]:
                course_to_indegree[neighbor] -= 1
                if course_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) == numCourses:
            return order
        return []
