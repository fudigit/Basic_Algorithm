'''
dfs

1. convert the string into a list of letters, so it can sorted
2, find all purmutations of the list of letter
3. when appending to final result, join the list of letters in one string

Slow!
'''

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        
        results = []
        if str is None:
            return results
        # str = [], resultswill out put [[]]
        
        str_list = sorted(list(str))
        # generate boolean list for str_list
        visited = [False] * len(str_list)
        self.dfs_permute(str_list, visited, [], results)
        return results


    # find all permuation starts with certain permutation
    def dfs_permute(self, str_list, visited, permutation, results):
        
        #exit
        n = len(str_list)
        if len(permutation) == n:
            # deepcopy when full sequence is generated
            results.append(''.join(permutation))
            return
            
        for i in range(0, n):
            # skip selected elements
            if visited[i]:
                continue
            
            # same as the previous number, with the previous not visited: create dup path
            if i > 0 and str_list[i] == str_list[i-1] and visited[i-1] is False:
                continue
            
            permutation.append(str_list[i])
            visited[i] = True

            self.dfs_permute(str_list, visited, permutation, results)
            visited[i] = False
            permutation.pop()
                    
    
