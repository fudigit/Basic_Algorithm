class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        results = []
        if s is None:
            return results
        
        self.dfs_partition(s, [], results)
        return results
            
    def dfs_partition(self, s, subStringList, results):
        if len(s) == 0:
            results.append(list(subStringList))
            return
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix) is False:
                continue
            elif self.is_palindrome(prefix) is True:
                subStringList.append(prefix)
                self.dfs_partition(s[i:], subStringList, results)
                subStringList.pop()
            
    def is_palindrome(self, s):
        return s == s[::-1]
        
