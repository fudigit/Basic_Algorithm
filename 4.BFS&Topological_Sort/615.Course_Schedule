from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        
        #uni_pre = set(prerequisites)
        
        for i in range(numCourses):
            print(i)
            # bfs for each course, if a ring is find, then false
            queue = deque([i])
            visited = set([i])
            
            while queue:
                print(queue, visited)
                course = queue.popleft()
                
                for pair in prerequisites:
                    if course == pair[1]:
                        course_next = pair[0]
                        if course_next in visited:
                            return False
                        visited.add(course_next)
                        queue.append(course_next)
                        
        return True
