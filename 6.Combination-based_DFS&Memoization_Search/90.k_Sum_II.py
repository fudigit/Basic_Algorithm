class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        results = []
        if A is None or target is None:
            return results
        
        A = sorted(list(A)) # set is use to rid of unique
        #self.level = 0      #check tree depth
        self.dfs(A, k, target, 0, [], results)
        return results
        
    def dfs(self, A, k, target, start, combination, results):
        #self.level += 1
        if target == 0 and k == 0:
            return results.append(list(combination)) # return, so no need to start another loop
            
        for i in range(start, len(A)):
            #print('i=', i, 'candi=',A[i], 'target=', target, 'start=', start, combination, 'level=', self.level)

            if target < A[i] or k < 0:
                return
            
            combination.append(A[i])
            self.dfs(A, k - 1, target - A[i], i + 1, combination, results)
            combination.pop()
            #self.level -= 1
        
