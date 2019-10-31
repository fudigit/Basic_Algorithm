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

    
# 二刷:
# 1. 拓扑排序的定义忘了
# 2. 如果不把问题转化为图的形式, 找到入度为0的点，就需要O(n*m). 对每个course，遍历prerequite里m种关系
#  -但是拓扑排序的时间复杂度是O(n + m), aka: O(Vertex + Edge)，所以需要预处理


#from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # course to indegrees: {0:0, 1:1, 2:1, 3:2}
        course_indegrees = {i:0 for i in range(numCourses)} #how many dependencies
        for pair in prerequisites:
            course_indegrees[pair[0]] += 1
        
        # preq course to current course: {0:[1,2], 1:[3], 2:[3]}
        neighbors = {i:[] for i in range(numCourses)}
        for cur, pre in prerequisites:
            neighbors[pre].append(cur)
        
        # add those course that has indegree of 0 to queue
        start_nodes = [c for c in course_indegrees if course_indegrees[c] == 0]
        queue = collections.deque(start_nodes)
        order = []
        
        # kill the course with indegree of 0, which reduce the indgree of the next courses by 1
        while queue:
            course = queue.popleft()
            order.append(course)
            
            for next_course in neighbors[course]:
                course_indegrees[next_course] -= 1 
                if course_indegrees[next_course] == 0:
                    queue.append(next_course)
            
        if len(order) == numCourses:
            return order
        
        return []
