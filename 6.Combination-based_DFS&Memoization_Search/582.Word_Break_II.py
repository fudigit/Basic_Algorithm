'''
use divide and conquer, similar to finding binary tree path
1. find all paritions given the current s
2. to see if a partition is valid, get the prefix and check if it's in the dict
3. memo search to avoid dups

- exist condition: be careful when partition go towards end of the string
- why memory can avoid the dups?
'''

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        memo = {}
        partitions = self.dfs(s, wordDict, memo)
        return partitions
    
    # find all valid partitions of s, and return all the paritions
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if s == []:
            return []
        
        partitions = []
        
        # when shall i starts? deal loop if i starts at 0
        for i in range(1, len(s)):
            prefix = s[:i]
            #print(prefix, partitions)
            if prefix not in wordDict:
                continue
            
            # if found the prefix in dict, what's all the partitions in s[i:]?
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            #print(sub_partitions)
            #sub_partitions are found, what should the paritions look like? Separate by " "
            for sub_partition in sub_partitions:
                #print(prefix,'prefix',sub_partition)
                partitions.append(prefix + " " + sub_partition)
        
        # necessary step: other paritions has no initial string (last char not used)
        if s in wordDict:
            partitions.append(s)
        
        memo[s] = partitions
        
        return partitions
        
        
# 找出整条路径，然后一次性加入到partitions里        
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        
        partition = []
        partitions = []
        memo1 = {}
        self.dfs(s, 0, partition, partitions, wordDict, memo1)
        return partitions
    
    
    
    def dfs(self, s, index, partition, partitions, wordDict, memo):
        if index == len(s):
            partitions.append(' '.join(partition[:]))
            return
        
        
        
        for i in range(index, len(s)):
            word = s[index:i + 1]
            if word not in wordDict:
                continue
            
            partition.append(word)
            self.dfs(s, i + 1, partition, partitions, wordDict, memo)
            partition.pop()
            
        memo[index] = partition
